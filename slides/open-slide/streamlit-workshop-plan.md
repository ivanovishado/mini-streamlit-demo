# Streamlit Workshop Slide Content Plan

## Summary

Create a new Spanish, from-scratch open-slide deck for a 4-hour, 2-day in-person Streamlit workshop that companions `/Users/igalaviz/Documents/dev/streamlit-demo/streamlit_app.py`.

The deck should teach one core arc: **Pandas analysis -> Streamlit widgets -> interactive local dashboard -> deployment preview**. It will frame the hands-on work as **individual**: each student builds and explains their own local app using the temporary dataset in `data/estudiantes_ai.csv`.

## Research Basis

- Streamlit's official fundamentals emphasize the fast edit/run loop, top-to-bottom reruns, widgets as Python variables, dataframes, charts, layout, and caching: https://docs.streamlit.io/get-started/fundamentals/main-concepts
- The official tutorial sequence moves from data inspection to charts and interactivity: https://docs.streamlit.io/get-started/tutorials/create-an-app
- The current app uses Streamlit's newer `st.Page` / `st.navigation` pattern, aligned with the docs' preferred multipage approach: https://docs.streamlit.io/develop/concepts/multipage-apps/overview
- Deployment preview should stay conceptual: dependencies, secrets, and remote `streamlit run`, based on https://docs.streamlit.io/deploy/concepts

## Deck Shape

- Slide id: `streamlit-workshop`.
- Target length: 22 slides.
- Language: Spanish teaching copy, with API names/code in English.
- Hands-on style: guided individual checkpoints with starter file, goal, expected output, and debrief.
- Setup depth: full setup block early in Day 1.
- Optional topic: deployment preview, not AI bonus.
- Visual/theme: no existing theme; visual style intentionally deferred. Default implementation later: classroom-friendly "data-lab poster" unless changed.

## Proposed Outline

1. Cover: "Streamlit: de analisis de datos a web app local".
2. Workshop promise: by the end, each student has a filterable local dashboard.
3. Two-day map: Day 1 UI + reruns; Day 2 Pandas + dashboard + deploy preview.
4. Setup checklist: venv, install requirements, run `streamlit run streamlit_app.py`.
5. What is Streamlit?: Python script as app canvas.
6. Mental model: top-to-bottom rerun on code change or widget interaction.
7. First app checkpoint: `exercises/day1/01_first_app.py`.
8. Text and feedback primitives: `st.title`, `st.write`, `st.markdown`, `st.success`.
9. Widgets as variables: button, slider, selectbox.
10. Widget checkpoint: `exercises/day1/02_widgets.py`.
11. Day 1 checkpoint: explain `widget -> variable -> output`.
12. Day 2 recap: what Pandas analysis already gives us.
13. Dataset map: columns in `estudiantes_ai.csv` and what each can answer.
14. Filter pattern: `input -> condition -> filtered dataframe`.
15. Pandas filter checkpoint: `exercises/day2/01_pandas_filters.py`.
16. Showing data: `st.dataframe`, `st.metric`, `st.bar_chart`.
17. Layout for analysis apps: sidebar filters, main area results, columns for KPIs.
18. Reference app walkthrough: intro, components, filters, capstone pages.
19. Capstone build plan: complete `exercises/day2/02_capstone_starter.py`.
20. Capstone success criteria: filters work, metrics update, chart updates, table exports.
21. Deployment preview: GitHub repo, requirements, secrets, Streamlit Community Cloud concept.
22. Closing: replace provisional data with Week 3 data and adapt filters, not the whole app.

## Test And Acceptance Criteria

- The outline fits two 2-hour sessions with clear individual checkpoints and debriefs.
- Every hands-on slide points to an existing local file or current app behavior.
- The deck does not depend on unavailable Week 3 analysis.
- Each student can explain their final app in 60 seconds: data source, controls, filtered output, decision enabled.
- Later implementation should only create `slides/streamlit-workshop/index.tsx` and optional slide-specific assets.
