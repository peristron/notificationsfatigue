"""Notification Fatigue: a monolithic Streamlit presentation app."""

from __future__ import annotations

from html import escape
from typing import Any

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(
    page_title="notification fatigue",
    layout="wide",
    initial_sidebar_state="auto",
)


# -----------------------------------------------------------------------------
# App configuration and presentation content
# -----------------------------------------------------------------------------

APP_TITLE = "notification fatigue"
APP_SUBTITLE = "when everything asks for attention, nothing feels important"
DATA_STATUS = "illustrative scenario model - not a measured research finding"

ACTIVE_THEME = st.context.theme.type

if ACTIVE_THEME == "dark":
    PALETTE = {
        "ink": "#F4F2EC",
        "muted": "#A6B0B7",
        "paper": "#0D1317",
        "panel": "#151D22",
        "signal": "#49C6B8",
        "noise": "#FF7B64",
        "accent": "#F2C14E",
        "grid": "#334149",
        "white": "#FFFFFF",
    }
else:
    PALETTE = {
        "ink": "#17242D",
        "muted": "#66737B",
        "paper": "#F7F5EF",
        "panel": "#EEEAE1",
        "signal": "#0F766E",
        "noise": "#D85E47",
        "accent": "#D7A91E",
        "grid": "#D6D2C8",
        "white": "#FFFFFF",
    }


SOURCE_NOTES = {
    1: {
        "label": "source presentation: notification overload",
        "supports": (
            "the source deck frames notification fatigue as overload created by excessive, "
            "repetitive, irrelevant, or poorly timed notifications, with disengagement and "
            "reduced attention as central risks."
        ),
        "note": (
            "the deck also contains several specific numerical claims about response, retention, "
            "frequency, timing, and click-through rates. those figures are intentionally not "
            "treated as measured facts in this app unless independently verified."
        ),
    },
    2: {
        "label": "source presentation: relevance and personalization",
        "supports": (
            "the source deck recommends context-aware notifications, user-controlled preferences, "
            "and personalization to reduce overload and increase perceived relevance."
        ),
        "note": "used here as design guidance rather than as a universal causal formula.",
    },
    3: {
        "label": "source presentation: timing",
        "supports": (
            "the source deck argues that notification timing affects receptivity and that poorly "
            "timed alerts can become interruptions rather than useful prompts."
        ),
        "note": (
            "specific timing windows in the original slides are not presented here as universal "
            "benchmarks."
        ),
    },
    4: {
        "label": "source presentation: concise, empathetic content",
        "supports": (
            "the source deck recommends concise notification content and supportive language so "
            "users can understand the message quickly without unnecessary friction."
        ),
        "note": (
            "specific character-count and click-through claims from the original deck are not "
            "repeated as measured findings in this app."
        ),
    },
    5: {
        "label": "source presentation: monitor and iterate",
        "supports": (
            "the source deck recommends tracking engagement, opt-outs, open/response behavior, and "
            "testing frequency, timing, and content rather than treating notification design as static."
        ),
        "note": "used as a practical product-design recommendation.",
    },
}


SECTIONS = [
    {
        "id": "fatigue",
        "nav_label": "1. Notification Fatigue",
        "eyebrow": "START HERE",
        "title": "When everything asks for attention, nothing feels important.",
        "lead": (
            "Notifications are supposed to help us notice what matters. The problem starts when "
            "the system asks for attention so often that the request itself loses meaning. {cite:1}"
        ),
        "paragraphs": [
            (
                "That is the core tension behind notification fatigue: useful prompts compete with "
                "repetitive, irrelevant, or badly timed alerts until the whole stream begins to feel "
                "like background noise."
            ),
            (
                "This isn't really a presentation about turning notifications off. It's a discussion "
                "about preserving their value."
            ),
        ],
        "callout_type": "info",
        "callout": "A notification has value only while the user still believes notifications are worth noticing.",
        "citations": [1],
    },
    {
        "id": "noise",
        "nav_label": "2. How Useful Becomes Noise",
        "eyebrow": "THE FAILURE MODE",
        "title": "Helpful nudges can quietly become a wall of interruptions.",
        "lead": (
            "Volume matters, but volume is only part of the problem. Timing, repetition, and "
            "relevance all affect whether a notification feels useful or intrusive. {cite:1}"
        ),
        "paragraphs": [
            (
                "A message can be important in isolation and still contribute to fatigue when it "
                "arrives beside too many other demands for attention."
            ),
            (
                "In other words, users don't experience each alert separately. They experience the "
                "whole stream."
            ),
        ],
        "callout_type": "warning",
        "callout": "The problem is rarely one notification. It's the accumulated attention claim.",
        "citations": [1],
    },
    {
        "id": "signal",
        "nav_label": "3. Signal vs. Noise",
        "eyebrow": "THE CENTERPIECE",
        "title": "The notification stream is a signal-to-noise system.",
        "lead": (
            "Every alert is effectively making a claim: 'this deserves your attention now.' If too "
            "many low-value claims arrive, the signal gets harder to trust."
        ),
        "paragraphs": [
            (
                "That makes notification fatigue partly structural. The more often the system asks "
                "for attention without delivering corresponding value, the less meaningful the next "
                "request can feel."
            ),
            (
                "Use the controls here as a thought experiment, not as a prediction. The goal is to "
                "make the shape of the problem visible."
            ),
        ],
        "callout_type": "info",
        "callout": "The exact numbers are illustrative. The useful question is how quickly low-value alerts can dominate the stream.",
        "citations": [1],
    },
    {
        "id": "sweetspot",
        "nav_label": "4. Finding the Sweet Spot",
        "eyebrow": "FREQUENCY",
        "title": "More communication is not automatically more communication value.",
        "lead": (
            "The source material recommends avoiding notification overload and finding a frequency "
            "that preserves usefulness without overwhelming the user. {cite:1}"
        ),
        "paragraphs": [
            (
                "There probably isn't one universal 'correct' number. Different products, audiences, "
                "tasks, and urgency levels create different tolerances."
            ),
            (
                "So the more practical question is: at what point does another notification add less "
                "value than attention cost?"
            ),
        ],
        "callout_type": "info",
        "callout": "Think in terms of marginal value: what does the next notification add that the previous one did not?",
        "citations": [1],
    },
    {
        "id": "relevance",
        "nav_label": "5. Relevance Beats Volume",
        "eyebrow": "CONTEXT",
        "title": "The best notification is not just timely. It is relevant to this user.",
        "lead": (
            "The source deck emphasizes context-aware messages, personalization, and user-controlled "
            "preferences as ways to reduce overload. {cite:2}"
        ),
        "paragraphs": [
            (
                "A generic alert asks every user to spend attention. A contextual alert earns that "
                "attention by connecting to something the user actually needs, did, missed, or is "
                "about to do."
            ),
            (
                "User control matters too. Preferences can turn notification design from something "
                "done to the user into something partly configured by the user."
            ),
        ],
        "callout_type": "info",
        "callout": "Relevance is not decoration. It is part of the attention bargain.",
        "citations": [2],
    },
    {
        "id": "timing",
        "nav_label": "6. Timing Is Part of the Message",
        "eyebrow": "WHEN",
        "title": "The same message can feel useful or disruptive depending on when it arrives.",
        "lead": (
            "The source material treats timing as part of notification quality, not as a separate "
            "delivery detail. {cite:3}"
        ),
        "paragraphs": [
            (
                "A well-written message can still fail if it lands at the wrong moment. Urgency, user "
                "state, sleep, focus, active work, and recent activity all change the context in which "
                "the alert is received."
            ),
            (
                "That suggests a useful design question: should this message be sent now, later, "
                "batched, or not at all?"
            ),
        ],
        "callout_type": "warning",
        "callout": "Timing is not just logistics. Timing changes the meaning of the interruption.",
        "citations": [3],
    },
    {
        "id": "design",
        "nav_label": "7. Designing the System",
        "eyebrow": "CONTENT + FEEDBACK",
        "title": "Notification quality is a system, not a sentence.",
        "lead": (
            "The source deck combines two practical ideas: keep messages concise and empathetic, and "
            "continuously monitor whether the strategy is actually working. {cite:4} {cite:5}"
        ),
        "paragraphs": [
            (
                "That means content design, frequency, timing, relevance, preferences, and analytics "
                "all belong to the same system. Improving only one dimension may not fix the overall experience."
            ),
            (
                "A/B testing, opt-out behavior, open/response patterns, and qualitative feedback can "
                "help reveal where the system is creating value and where it is simply creating noise."
            ),
        ],
        "callout_type": "info",
        "callout": "Don't just send notifications. Instrument the notification system and learn from how people respond.",
        "citations": [4, 5],
    },
    {
        "id": "takeaways",
        "nav_label": "8. Takeaways",
        "eyebrow": "WHAT TO REMEMBER",
        "title": "Protect the signal, not the volume.",
        "lead": (
            "Notification fatigue is less about whether alerts exist and more about whether the "
            "attention they consume keeps producing enough value."
        ),
        "paragraphs": [
            (
                "Useful notification systems tend to be selective, contextual, timely, concise, "
                "configurable, and measurable. {cite:2} {cite:3} {cite:4} {cite:5}"
            ),
            (
                "The design goal is not maximum reach. It is sustained trust in the stream."
            ),
        ],
        "callout_type": "info",
        "callout": "If every message is urgent, urgency becomes meaningless. If every alert matters, fewer alerts may actually matter more.",
        "citations": [2, 3, 4, 5],
    },
    {
        "id": "sources",
        "nav_label": "Sources & evidence notes",
        "eyebrow": "EVIDENCE NOTES",
        "title": "What this app preserves from the source decks - and what it deliberately softens.",
        "lead": (
            "The app preserves the source presentations' core structure and recommendations while "
            "avoiding several precise numerical claims that were not independently verified here."
        ),
        "paragraphs": [
            (
                "The original decks include specific figures for response rates, retention, ideal "
                "frequency, timing windows, and click-through improvements. Those figures may be useful "
                "starting points for further research, but this app does not present them as established facts."
            ),
            (
                "The signal-to-noise simulator is intentionally illustrative. Its purpose is to help "
                "an audience reason about structure and direction, not to predict user behavior."
            ),
        ],
        "callout_type": "warning",
        "callout": "Treat the simulator and any scenario values as discussion tools, not measured findings.",
        "citations": [],
    },
]

LIVE_SECTION_IDS = [section["id"] for section in SECTIONS if section["id"] != "sources"]

SUMMARY_POINTS = [
    "volume is only one source of fatigue; relevance, timing, and repetition matter too.",
    "a notification stream behaves like a signal-to-noise system.",
    "user control and context can preserve trust in the stream.",
    "timing changes whether an alert feels useful or disruptive.",
    "measure the system, not just the send count.",
]


# -----------------------------------------------------------------------------
# Visuals
# -----------------------------------------------------------------------------


def signal_noise_chart(total_notifications: int, relevant_percent: int) -> go.Figure:
    relevant = round(total_notifications * relevant_percent / 100)
    noise = total_notifications - relevant

    figure = go.Figure()
    figure.add_trace(
        go.Bar(
            x=["notification stream"],
            y=[relevant],
            name="signal",
            marker_color=PALETTE["signal"],
            hovertemplate=f"{relevant} relevant alerts<extra></extra>",
        )
    )
    figure.add_trace(
        go.Bar(
            x=["notification stream"],
            y=[noise],
            name="noise",
            marker_color=PALETTE["noise"],
            hovertemplate=f"{noise} low-value alerts<extra></extra>",
        )
    )
    figure.update_layout(
        barmode="stack",
        height=390,
        margin={"l": 20, "r": 20, "t": 20, "b": 20},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"family": "Arial, sans-serif", "color": PALETTE["ink"], "size": 15},
        legend={"orientation": "h", "y": 1.12, "x": 0},
        xaxis={"showgrid": False, "showticklabels": False},
        yaxis={"title": "illustrative alerts per day", "gridcolor": PALETTE["grid"], "rangemode": "tozero"},
    )
    return figure



def sweet_spot_curve() -> go.Figure:
    x = list(range(1, 13))
    value = [24, 42, 57, 68, 75, 79, 78, 73, 65, 54, 41, 27]
    figure = go.Figure(
        go.Scatter(
            x=x,
            y=value,
            mode="lines+markers",
            line={"color": PALETTE["signal"], "width": 5, "shape": "spline"},
            marker={"size": 9, "color": PALETTE["accent"]},
            fill="tozeroy",
            fillcolor="rgba(73,198,184,0.12)",
            hovertemplate="%{x} alerts/day<br>illustrative value index %{y}<extra></extra>",
        )
    )
    figure.update_layout(
        height=430,
        margin={"l": 20, "r": 20, "t": 20, "b": 20},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        font={"family": "Arial, sans-serif", "color": PALETTE["ink"], "size": 15},
        xaxis={"title": "illustrative notifications per day", "showgrid": False},
        yaxis={"title": "illustrative communication value", "gridcolor": PALETTE["grid"], "range": [0, 90]},
    )
    return figure



def timing_windows_visual():
    figure, axis = plt.subplots(figsize=(12, 4.6))
    figure.patch.set_alpha(0)
    axis.set_facecolor("none")
    axis.set_xlim(0, 24)
    axis.set_ylim(0, 1)
    axis.axis("off")

    windows = [
        (0, 7, "sleep / unavailable", PALETTE["noise"]),
        (7, 9, "transition", PALETTE["accent"]),
        (9, 12, "focus-heavy work", PALETTE["noise"]),
        (12, 14, "lower-friction window", PALETTE["signal"]),
        (14, 17, "focus-heavy work", PALETTE["noise"]),
        (17, 21, "context-dependent", PALETTE["accent"]),
        (21, 24, "wind-down", PALETTE["noise"]),
    ]

    for start, end, label, color in windows:
        axis.add_patch(
            plt.Rectangle((start, 0.28), end - start, 0.38, facecolor=color, alpha=0.85)
        )
        axis.text(
            (start + end) / 2,
            0.47,
            label,
            ha="center",
            va="center",
            fontsize=9,
            color=PALETTE["white"] if color != PALETTE["accent"] else PALETTE["ink"],
            fontweight="bold",
        )

    for hour in range(0, 25, 3):
        axis.text(hour, 0.16, f"{hour:02d}:00", ha="center", va="center", color=PALETTE["muted"], fontsize=9)

    axis.text(
        0,
        0.88,
        "illustrative day: the same notification can land very differently depending on context",
        fontsize=16,
        fontweight="bold",
        color=PALETTE["ink"],
    )
    axis.text(
        0,
        0.04,
        "example only: user context, urgency, role, and product behavior should determine actual timing logic.",
        fontsize=9,
        color=PALETTE["muted"],
    )
    figure.subplots_adjust(left=0.03, right=0.98, top=0.95, bottom=0.08)
    return figure


# -----------------------------------------------------------------------------
# UI helpers
# -----------------------------------------------------------------------------


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        :root {
            --ink:var(--text-color);
            --muted:color-mix(in srgb, var(--text-color) 66%, transparent);
            --signal:#49C6B8;
            --noise:var(--primary-color);
            --accent:#F2C14E;
            --line:color-mix(in srgb, var(--text-color) 20%, transparent);
            --panel:color-mix(in srgb, var(--text-color) 6%, var(--background-color));
        }
        html, body {
            -webkit-text-size-adjust:100%;
            text-size-adjust:100%;
        }
        body { text-transform:lowercase; }
        .stApp { background:var(--background-color); color:var(--text-color); }
        [data-testid="stHeader"] {
            background:color-mix(in srgb, var(--background-color) 88%, transparent);
        }
        [data-testid="stSidebar"] {
            background-color:var(--secondary-background-color, var(--background-color))!important;
            z-index:999999!important;
            isolation:isolate;
        }
        [data-testid="stSidebar"] > div,
        [data-testid="stSidebarContent"] {
            background-color:var(--secondary-background-color, var(--background-color))!important;
            opacity:1!important;
        }
        .block-container { max-width:1380px; padding-top:2.4rem; padding-bottom:3rem; }
        .section-rule { border-top:1px solid var(--line); margin:.6rem 0 1.7rem; }
        .eyebrow { color:var(--noise); font-size:.78rem; font-weight:800; letter-spacing:.14em; }
        .display-title { color:var(--ink); font-size:4.8rem; line-height:.98;
                         font-weight:800; max-width:1050px; margin:.55rem 0 1.2rem; }
        .lead { color:var(--ink); font-size:1.62rem; line-height:1.45;
                max-width:980px; margin-bottom:1.6rem; }
        .body-copy { color:var(--ink); font-size:1.12rem; line-height:1.68; max-width:850px; }
        .progress-copy { color:var(--muted); font-size:.85rem; font-weight:700; }
        .data-label { display:inline-block; background:var(--panel); color:var(--ink);
                      border-left:4px solid var(--accent); padding:.45rem .75rem;
                      margin:.4rem 0 1rem; font-size:.82rem; font-weight:800; }
        .footnotes { border-top:1px solid var(--line); margin-top:2rem; padding-top:1rem; }
        .footnotes,.footnotes p { color:var(--muted); font-size:.83rem; line-height:1.5; }
        .source-item { padding:1rem 0; border-bottom:1px solid var(--line); }
        .source-label { color:var(--noise); font-weight:800; }
        .source-evidence { color:var(--muted); margin-top:.45rem; line-height:1.5; }
        .summary-line { border-top:1px solid var(--line); padding:.9rem 0; font-size:1.12rem; }
        .metric-strip { display:grid; grid-template-columns:repeat(3,1fr); border-top:1px solid var(--line);
                        border-bottom:1px solid var(--line); margin-top:1rem; }
        .metric-item { padding:1rem .85rem; border-right:1px solid var(--line); }
        .metric-item:last-child { border-right:0; }
        .metric-value { display:block; color:var(--ink); font-size:1.65rem; font-weight:850; }
        .metric-label { color:var(--muted); font-size:.78rem; font-weight:750; }
        .notification-stage { border-top:1px solid var(--line); border-bottom:1px solid var(--line);
                              padding:1rem 0; margin-top:.25rem; }
        .notification-kicker { color:var(--muted); font-size:.75rem; font-weight:800;
                               letter-spacing:.12em; margin-bottom:.5rem; }
        .notification-card { position:relative; display:grid; grid-template-columns:2.2rem 1fr auto;
                             align-items:center; gap:.8rem; min-height:3.7rem;
                             border-top:1px solid var(--line); opacity:.5;
                             animation:notification-pulse 5s infinite; }
        .notification-card:nth-child(2){animation-delay:1s}
        .notification-card:nth-child(3){animation-delay:2s}
        .notification-card:nth-child(4){animation-delay:3s}
        .notification-card:nth-child(5){animation-delay:4s}
        .notification-number { font-size:.76rem; font-weight:800; color:var(--noise); }
        .notification-name { font-size:1.05rem; font-weight:800; color:var(--ink); }
        .notification-state { font-size:.8rem; color:var(--muted); font-weight:700; }
        .notification-card::after { content:""; position:absolute; left:0; bottom:-1px; height:3px;
                                    width:100%; background:var(--noise); transform:scaleX(0);
                                    transform-origin:left; animation:notification-line 5s infinite; }
        .notification-card:nth-child(2)::after{animation-delay:1s}
        .notification-card:nth-child(3)::after{animation-delay:2s}
        .notification-card:nth-child(4)::after{animation-delay:3s}
        .notification-card:nth-child(5)::after{animation-delay:4s}
        @keyframes notification-pulse {
            0%,16% { opacity:1; transform:translateX(.35rem); }
            22%,100% { opacity:.5; transform:translateX(0); }
        }
        @keyframes notification-line {
            0% { transform:scaleX(0); }
            5%,16% { transform:scaleX(1); }
            22%,100% { transform:scaleX(0); }
        }
        div[data-testid="stButton"]>button { min-height:3rem; font-weight:750; border-radius:4px; }
        div[data-testid="stButton"]>button[kind="primary"] { background:var(--noise); border-color:var(--noise); }
        [data-testid="stHorizontalBlock"] > [data-testid="stColumn"] { min-width:0; }
        @media(max-width:1000px) {
            .display-title{font-size:3.5rem;line-height:1.04}
            .lead{font-size:1.38rem}
        }
        @media(max-width:700px) {
            .block-container{max-width:100%;padding:1.1rem 1rem 2.25rem!important}
            .display-title{font-size:2.3rem;line-height:1.08;margin:.45rem 0 1rem;overflow-wrap:break-word}
            .lead{font-size:1.08rem;line-height:1.5;margin-bottom:1.25rem}
            .body-copy{font-size:1rem;line-height:1.62;max-width:100%}
            .body-copy p{margin:0 0 1rem}
            .eyebrow,.progress-copy{font-size:.7rem}
            .data-label{font-size:.74rem;line-height:1.4;max-width:100%}
            .metric-strip{grid-template-columns:1fr}
            .metric-item{border-right:0;border-bottom:1px solid var(--line)}
            .notification-card{grid-template-columns:1.8rem minmax(0,1fr)}
            .notification-state{grid-column:2}
            .footnotes,.footnotes p,.source-item{font-size:.76rem;line-height:1.55;overflow-wrap:anywhere}
            [data-testid="stSidebar"]{max-width:min(88vw,21rem)!important}
            [data-testid="stSidebar"] *{overflow-wrap:break-word}
        }
        @media(prefers-reduced-motion:reduce) {
            .notification-card,.notification-card::after{animation:none}
        }
        @media print {
            [data-testid="stSidebar"],[data-testid="stHeader"],[data-testid="stButton"]{display:none!important}
            .block-container{max-width:none;padding:0}
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def section_by_id(section_id: str) -> dict[str, Any]:
    return next(section for section in SECTIONS if section["id"] == section_id)


def citation_marker(citation_id: int) -> str:
    label = escape(SOURCE_NOTES[citation_id]["label"])
    return f'<sup><a href="#source-{citation_id}" title="{label}">[{citation_id}]</a></sup>'


def render_citations(text: str) -> str:
    rendered = escape(text)
    for citation_id in SOURCE_NOTES:
        rendered = rendered.replace(escape(f"{{cite:{citation_id}}}"), citation_marker(citation_id))
    return rendered


def go_to(section_id: str) -> None:
    st.session_state.active_section = section_id
    st.session_state.section_picker = section_id


def render_endnotes(citation_ids: list[int]) -> None:
    if not citation_ids:
        return
    lines = ["<div class='footnotes'><strong>section source notes</strong>"]
    for citation_id in citation_ids:
        item = SOURCE_NOTES[citation_id]
        lines.append(
            f"<p id='source-{citation_id}'><strong>[{citation_id}]</strong> "
            f"<span class='source-label'>{escape(item['label'])}</span><br>"
            f"{escape(item['supports'])}<br><em>{escape(item['note'])}</em></p>"
        )
    st.markdown("".join(lines) + "</div>", unsafe_allow_html=True)


def render_visual(section_id: str) -> None:
    if section_id == "fatigue":
        st.markdown(
            """
            <div class="notification-stage">
                <div class="notification-kicker">ATTENTION CLAIMS ARRIVING</div>
                <div class="notification-card">
                    <span class="notification-number">01</span>
                    <span class="notification-name">deadline reminder</span>
                    <span class="notification-state">possibly useful</span>
                </div>
                <div class="notification-card">
                    <span class="notification-number">02</span>
                    <span class="notification-name">team update</span>
                    <span class="notification-state">maybe later</span>
                </div>
                <div class="notification-card">
                    <span class="notification-number">03</span>
                    <span class="notification-name">promotional message</span>
                    <span class="notification-state">low relevance</span>
                </div>
                <div class="notification-card">
                    <span class="notification-number">04</span>
                    <span class="notification-name">duplicate reminder</span>
                    <span class="notification-state">already seen</span>
                </div>
                <div class="notification-card">
                    <span class="notification-number">05</span>
                    <span class="notification-name">urgent alert</span>
                    <span class="notification-state">now competing with the rest</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif section_id == "noise":
        st.markdown(
            """
            <div class="metric-strip">
                <div class="metric-item">
                    <span class="metric-value">volume</span>
                    <span class="metric-label">how many attention claims arrive</span>
                </div>
                <div class="metric-item">
                    <span class="metric-value">relevance</span>
                    <span class="metric-label">how much value each claim carries</span>
                </div>
                <div class="metric-item">
                    <span class="metric-value">timing</span>
                    <span class="metric-label">when the claim interrupts the user</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("#### a useful way to think about it")
        st.info("fatigue can emerge when the attention cost of the stream grows faster than the value delivered by the stream.")

    elif section_id == "signal":
        st.markdown(f"<div class='data-label'>{DATA_STATUS}</div>", unsafe_allow_html=True)
        total_notifications = st.slider("notifications received per day", 3, 60, 24, 1)
        relevant_percent = st.slider("percent that feel genuinely relevant", 5, 100, 30, 5)
        protected_focus_percent = st.slider("percent arriving during protected-focus time", 0, 100, 35, 5)

        relevant = round(total_notifications * relevant_percent / 100)
        low_value = total_notifications - relevant
        focus_interruptions = round(total_notifications * protected_focus_percent / 100)

        st.plotly_chart(
            signal_noise_chart(total_notifications, relevant_percent),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown(
            f"""
            <div class="metric-strip">
                <div class="metric-item">
                    <span class="metric-value">{relevant}</span>
                    <span class="metric-label">illustrative signal</span>
                </div>
                <div class="metric-item">
                    <span class="metric-value">{low_value}</span>
                    <span class="metric-label">illustrative low-value alerts</span>
                </div>
                <div class="metric-item">
                    <span class="metric-value">{focus_interruptions}</span>
                    <span class="metric-label">arriving during protected-focus time</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif section_id == "sweetspot":
        st.markdown(f"<div class='data-label'>{DATA_STATUS}</div>", unsafe_allow_html=True)
        st.plotly_chart(sweet_spot_curve(), use_container_width=True, config={"displayModeBar": False})
        st.caption(
            "the curve is conceptual: too few messages can miss useful opportunities, while too many can dilute attention and trust."
        )

    elif section_id == "relevance":
        st.markdown("### same user, different notification quality")
        left, right = st.columns(2)
        with left:
            st.error("**generic:** you have activity waiting. check the app.")
            st.caption("asks for attention without explaining why it matters")
        with right:
            st.success("**contextual:** your assignment is due tomorrow. continue where you left off.")
            st.caption("connects the alert to the user's current context and next action")

    elif section_id == "timing":
        st.markdown(f"<div class='data-label'>{DATA_STATUS}</div>", unsafe_allow_html=True)
        figure = timing_windows_visual()
        st.pyplot(figure, use_container_width=True)
        plt.close(figure)

    elif section_id == "design":
        st.markdown("### a simple operating loop")
        st.markdown(
            """
            <div class="metric-strip">
                <div class="metric-item">
                    <span class="metric-value">1. send</span>
                    <span class="metric-label">with a clear reason and audience</span>
                </div>
                <div class="metric-item">
                    <span class="metric-value">2. observe</span>
                    <span class="metric-label">engagement, opt-outs, response patterns</span>
                </div>
                <div class="metric-item">
                    <span class="metric-value">3. adjust</span>
                    <span class="metric-label">frequency, timing, relevance, content</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("repeat the loop rather than assuming the initial notification strategy is permanently correct.")

    elif section_id == "takeaways":
        st.markdown("### some ideas to carry forward...")
        for point in SUMMARY_POINTS:
            st.markdown(f"<div class='summary-line'>{escape(point)}</div>", unsafe_allow_html=True)

    elif section_id == "sources":
        for citation_id, item in SOURCE_NOTES.items():
            st.markdown(
                f"<div class='source-item' id='source-{citation_id}'>"
                f"<span class='source-label'>[{citation_id}] {escape(item['label'])}</span>"
                f"<div class='source-evidence'><strong>what it supports:</strong> {escape(item['supports'])}</div>"
                f"<div class='source-evidence'><strong>evidence note:</strong> {escape(item['note'])}</div>"
                f"</div>",
                unsafe_allow_html=True,
            )


def render_navigation(is_reference_page: bool, current_index: int = 0) -> None:
    previous_column, _, next_column = st.columns([1, 2.2, 1])

    if is_reference_page:
        with next_column:
            st.button(
                "return to takeaways",
                type="primary",
                on_click=go_to,
                args=(LIVE_SECTION_IDS[-1],),
                use_container_width=True,
            )
        return

    with previous_column:
        if current_index > 0:
            st.button(
                "previous",
                on_click=go_to,
                args=(LIVE_SECTION_IDS[current_index - 1],),
                use_container_width=True,
            )

    with next_column:
        has_next = current_index < len(LIVE_SECTION_IDS) - 1
        next_id = LIVE_SECTION_IDS[current_index + 1] if has_next else LIVE_SECTION_IDS[0]
        st.button(
            "next" if has_next else "start again",
            type="primary",
            on_click=go_to,
            args=(next_id,),
            use_container_width=True,
        )


def render_presentation() -> None:
    current_id = st.session_state.active_section
    section = section_by_id(current_id)
    is_reference_page = current_id not in LIVE_SECTION_IDS

    if is_reference_page:
        st.markdown("<div class='progress-copy'>REFERENCE PAGE</div>", unsafe_allow_html=True)
        current_index = 0
    else:
        current_index = LIVE_SECTION_IDS.index(current_id)
        st.markdown(
            f"<div class='progress-copy'>SECTION {current_index + 1} OF {len(LIVE_SECTION_IDS)}</div>",
            unsafe_allow_html=True,
        )
        st.progress((current_index + 1) / len(LIVE_SECTION_IDS))

    render_navigation(is_reference_page, current_index)
    st.markdown("<div class='section-rule'></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='eyebrow'>{escape(section['eyebrow'])}</div>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='display-title'>{escape(section['title'])}</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='lead'>{render_citations(section['lead'])}</div>", unsafe_allow_html=True)

    copy_column, visual_column = st.columns([0.85, 1.35], gap="large")
    with copy_column:
        paragraphs = "".join(f"<p>{render_citations(text)}</p>" for text in section["paragraphs"])
        st.markdown(f"<div class='body-copy'>{paragraphs}</div>", unsafe_allow_html=True)
        (st.warning if section["callout_type"] == "warning" else st.info)(section["callout"])

    with visual_column:
        render_visual(current_id)

    render_endnotes(section["citations"])


# -----------------------------------------------------------------------------
# App entry point
# -----------------------------------------------------------------------------

inject_styles()

section_ids = [section["id"] for section in SECTIONS]
section_labels = {section["id"]: section["nav_label"] for section in SECTIONS}

if "active_section" not in st.session_state:
    st.session_state.active_section = section_ids[0]
if "section_picker" not in st.session_state:
    st.session_state.section_picker = section_ids[0]

if st.session_state.active_section not in section_ids:
    st.session_state.active_section = section_ids[0]
if st.session_state.section_picker not in section_ids:
    st.session_state.section_picker = st.session_state.active_section


def sync_sidebar() -> None:
    st.session_state.active_section = st.session_state.section_picker


with st.sidebar:
    st.markdown(f"## {APP_TITLE}")
    st.caption(APP_SUBTITLE)
    st.selectbox(
        "jump to section",
        options=section_ids,
        format_func=lambda section_id: section_labels[section_id],
        key="section_picker",
        on_change=sync_sidebar,
    )
    st.button("restart presentation", on_click=go_to, args=(section_ids[0],), use_container_width=True)
    st.markdown("---")
    st.caption("built from the supplied notification-fatigue presentation decks; precise numerical claims are softened unless verified.")

render_presentation()
