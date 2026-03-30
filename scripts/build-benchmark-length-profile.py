#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


ROOT = Path(__file__).resolve().parents[1]
MATERIALS_DIR = ROOT / "materials"
COUNTING_RULES_VERSION = "md-clean-transferable-v2"
RATIO_BANDS = {
    "short": {"min_ratio": 0.35, "target_ratio": 0.40, "max_ratio": 0.45},
    "medium": {"min_ratio": 0.55, "target_ratio": 0.625, "max_ratio": 0.70},
    "full": {"min_ratio": 0.75, "target_ratio": 0.825, "max_ratio": 0.90},
}
PAGE_MARKER = re.compile(r"(\d+)\s*/\s*(\d+)\s+\[Table_[^\]]+\]\s+")
SPACE_RE = re.compile(r"\s+")


@dataclass(frozen=True)
class Segment:
    page: int
    start: Optional[str] = None
    end: Optional[str] = None


BENCHMARKS = {
    "minimax": {
        "benchmark_id": "minimax-born-global-2026-02-10",
        "source_md_glob": "*MINIMAX*2026-02-10-3.md",
        "page_buckets": {
            "cover_front_page": [1],
            "toc_index": [2, 3, 4],
            "body": list(range(5, 35)),
            "detailed_financials": [35],
            "disclaimer_research_team": [36, 37],
        },
        "clean_full_segments": {
            "core_conclusions": [
                Segment(1, start="[Table_Summary]", end="[Table_Finance]")
            ],
            "company_overview": [Segment(page) for page in range(5, 15)],
            "industry_competition": [Segment(page) for page in range(15, 23)],
            "highlights_differentiation": [Segment(page) for page in range(23, 32)],
            "commercialization_boundary": [Segment(page) for page in range(32, 34)],
            "risks": [Segment(34)],
        },
        "transferable_segments": {
            "core_conclusions": [
                Segment(1, start="[Table_Summary]", end="[Table_Finance]")
            ],
            "company_overview": [Segment(page) for page in range(5, 15)],
            "industry_competition": [Segment(page) for page in range(15, 23)],
            "highlights_differentiation": [Segment(page) for page in range(23, 32)],
            "commercialization_boundary": [
                Segment(32, start="（一）业务拆分及盈利预测"),
                Segment(33, end="（二）估值分析与投资建议"),
            ],
            "risks": [Segment(34)],
        },
        "full_notes": [
            "保留首页核心观点与正文页，不计目录、图表索引、详细财务附表和免责声明。",
            "clean_full_report_chars 保留盈利预测和投资建议整章，因为它属于 sell-side 正文的一部分。",
        ],
        "transferable_notes": [
            "transferable_body_chars 删除首页财务摘要、评级区块、目标价语句和详细财务/估值壳。",
            "商业化与边界章节仅保留业务拆分、经营逻辑与费用结构，不保留 PS、目标价和评级建议。",
        ],
        "deep_extraction": {
            "front_page_density": "首页是压缩版 thesis tree，不是目录式摘要。前页应先给定位，再给模型/产品/商业化与全球化判断。",
            "chapter_opening_formula": "判断句 -> 机制展开 -> 图表/数据锚定 -> 对 thesis 的含义。",
            "evidence_architecture": "公司自有证据、第三方市场证据、经营验证信号、经济含义翻译四层递进。",
            "non_transferable_shells": [
                "上市公司评级语言",
                "PS 估值与目标价逻辑",
                "详细财务预测表",
                "股价和投资建议口径",
            ],
        },
    },
    "fourth-paradigm": {
        "benchmark_id": "fourth-paradigm-decision-intelligence-2024-12-03",
        "source_md_glob": "*第四范式*2024-12-03-3.md",
        "page_buckets": {
            "cover_front_page": [1],
            "toc_index": [2, 3, 4],
            "body": list(range(5, 49)),
            "detailed_financials": [49],
            "disclaimer_research_team": [50, 51],
        },
        "clean_full_segments": {
            "core_conclusions": [
                Segment(1, start="[Table_Summary]", end="[Table_Finance]"),
                Segment(5),
                Segment(6),
            ],
            "company_overview": [Segment(page) for page in range(7, 19)],
            "industry_competition": [Segment(page) for page in range(19, 27)],
            "highlights_differentiation": [Segment(page) for page in range(27, 42)],
            "commercialization_boundary": [Segment(page) for page in range(42, 48)],
            "risks": [Segment(48)],
        },
        "transferable_segments": {
            "core_conclusions": [
                Segment(1, start="[Table_Summary]", end="[Table_Finance]"),
                Segment(5),
                Segment(6),
            ],
            "company_overview": [Segment(page) for page in range(7, 19)],
            "industry_competition": [Segment(page) for page in range(19, 27)],
            "highlights_differentiation": [Segment(page) for page in range(27, 42)],
            "commercialization_boundary": [
                Segment(page) for page in range(42, 45)
            ]
            + [
                Segment(45),
                Segment(46, end="第四范式的可比公司包括"),
            ],
            "risks": [Segment(48)],
        },
        "full_notes": [
            "保留前页、投资要点页、正文、挑战章节与盈利预测章节，不计目录、索引、财务附表和免责声明。",
            "clean_full_report_chars 体现企业平台型 sell-side 深度报告的完整正文字数。",
        ],
        "transferable_notes": [
            "transferable_body_chars 删除评级、目标价、可比公司估值表和股票 call block。",
            "商业化与边界章节保留挑战约束与业务拆分逻辑，删除 PS 估值与买入评级结论。",
        ],
        "deep_extraction": {
            "front_page_density": "除了首页摘要，还单独使用投资要点页把 thesis 拆成多个层级，因此前页密度高于一般公司概况页。",
            "chapter_opening_formula": "先给定位与主问题，再用类比/对比章承接，再进入挑战与商业化边界。",
            "evidence_architecture": "产品架构、客户渗透、外部对标、挑战约束、预测翻译共同承担证据职责。",
            "non_transferable_shells": [
                "买入评级",
                "PS 估值和合理价值",
                "细项业务拆分预测表中的股票研究口径",
                "直接复用 Palantir 对比壳",
            ],
        },
    },
}


def collapse(text: str) -> str:
    return SPACE_RE.sub("", text)


def load_pages(path: Path) -> Dict[int, str]:
    text = path.read_text(encoding="utf-8")
    matches = list(PAGE_MARKER.finditer(text))
    if not matches:
        raise ValueError(f"无法在 {path} 中识别页码标记。")

    pages: Dict[int, str] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        page_num = int(match.group(1))
        pages[page_num] = collapse(text[start:end])
    return pages


def extract_segment(page_text: str, segment: Segment) -> str:
    start_index = 0
    end_index = len(page_text)

    if segment.start:
        start_index = page_text.find(segment.start)
        if start_index == -1:
            raise ValueError(f"未找到起始锚点：{segment.start}")

    if segment.end:
        end_index = page_text.find(segment.end, start_index)
        if end_index == -1:
            raise ValueError(f"未找到结束锚点：{segment.end}")

    return page_text[start_index:end_index]


def join_segments(pages: Dict[int, str], segments: List[Segment]) -> str:
    chunks = []
    for segment in segments:
        page_text = pages[segment.page]
        chunks.append(extract_segment(page_text, segment))
    return "".join(chunks)


def chapter_counts(
    pages: Dict[int, str], chapter_map: Dict[str, List[Segment]]
) -> Dict[str, int]:
    return {
        chapter: len(join_segments(pages, segments))
        for chapter, segments in chapter_map.items()
    }


def ratio_budget(base_chars: int) -> Dict[str, Dict[str, int]]:
    budgets = {}
    for band, ratios in RATIO_BANDS.items():
        budgets[band] = {
            key.replace("_ratio", ""): round(base_chars * value)
            for key, value in ratios.items()
        }
    return budgets


def chapter_budgets(
    base_chars: int, weights: Dict[str, float]
) -> Dict[str, Dict[str, Dict[str, int]]]:
    budgets: Dict[str, Dict[str, Dict[str, int]]] = {}
    total_budgets = ratio_budget(base_chars)
    for band, totals in total_budgets.items():
        budgets[band] = {}
        for chapter, weight in weights.items():
            budgets[band][chapter] = {
                label: round(total * weight) for label, total in totals.items()
            }
    return budgets


def rounded_weights(chapter_counts_map: Dict[str, int]) -> Dict[str, float]:
    total = sum(chapter_counts_map.values())
    return {
        chapter: round(chars / total, 4) if total else 0.0
        for chapter, chars in chapter_counts_map.items()
    }


def build_profile(benchmark_key: str) -> Dict[str, object]:
    config = BENCHMARKS[benchmark_key]
    source_md_path = next(MATERIALS_DIR.glob(config["source_md_glob"]))
    raw_text = source_md_path.read_text(encoding="utf-8")
    pages = load_pages(source_md_path)

    full_counts = chapter_counts(pages, config["clean_full_segments"])
    transferable_counts = chapter_counts(pages, config["transferable_segments"])
    weights = rounded_weights(transferable_counts)

    page_buckets = {
        bucket: {
            "pages": page_numbers,
            "chars": sum(len(pages[page]) for page in page_numbers),
        }
        for bucket, page_numbers in config["page_buckets"].items()
    }

    transferable_total = sum(transferable_counts.values())
    return {
        "benchmark_id": config["benchmark_id"],
        "source_md_path": str(source_md_path.relative_to(ROOT)).replace("\\", "/"),
        "counting_rules_version": COUNTING_RULES_VERSION,
        "raw_md_chars": len(collapse(raw_text)),
        "page_buckets": page_buckets,
        "clean_full_report_chars": sum(full_counts.values()),
        "transferable_body_chars": transferable_total,
        "clean_full_chapter_counts": full_counts,
        "transferable_chapter_counts": transferable_counts,
        "chapter_weight_profile": weights,
        "ratio_bands": RATIO_BANDS,
        "total_budget_by_band": ratio_budget(transferable_total),
        "chapter_budget_by_band": chapter_budgets(transferable_total, weights),
        "full_notes": config["full_notes"],
        "transferable_notes": config["transferable_notes"],
        "deep_extraction": config["deep_extraction"],
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a benchmark length profile from a local broker-report markdown extraction."
    )
    parser.add_argument(
        "--benchmark",
        required=True,
        choices=sorted(BENCHMARKS.keys()),
        help="Benchmark profile to build.",
    )
    parser.add_argument(
        "--output",
        help="Optional output path. If omitted, prints JSON to stdout.",
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print the JSON output.",
    )
    args = parser.parse_args()

    profile = build_profile(args.benchmark)
    payload = json.dumps(
        profile,
        ensure_ascii=False,
        indent=2 if args.pretty or args.output else None,
        sort_keys=False,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)


if __name__ == "__main__":
    main()
