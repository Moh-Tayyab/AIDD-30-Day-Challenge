# Tasks: 002-streamlit-calculator-ui

**Input**: Design documents from `/specs/002-streamlit-calculator-ui/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Install `streamlit` using `uv pip install streamlit`.
- [X] T002 Create the main Streamlit application file `app.py`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T003 Import necessary libraries (`streamlit`, `evaluate_expression`) in `app.py`.
- [X] T004 Set Streamlit page configuration (title, layout) in `app.py`.
- [X] T005 Initialize `st.session_state.expression` to an empty string in `app.py`.
- [X] T006 Initialize `st.session_state.result` to None or empty in `app.py`.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Display Current Expression and Result (Priority: P1) 🎯 MVP

**Goal**: The UI displays the current arithmetic expression being built and the results of evaluations.

**Independent Test**: A display area is visible and correctly updates with input and results.

### Implementation for User Story 1

- [X] T007 [US1] Create a display area for the current expression and results (e.g., `st.text_input` or `st.empty` with `st.markdown`) in `app.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Button Input for Expression Building (Priority: P1)

**Goal**: Users can build an expression by clicking on numerical digits, operators, and parentheses buttons.

**Independent Test**: Clicking number, operator, and parenthesis buttons correctly appends to the display.

### Implementation for User Story 2

- [X] T008 [P] [US2] Define a callback function for button clicks to handle appending values to `st.session_state.expression` in `app.py`.
- [X] T009 [P] [US2] Create number buttons (0-9, .) using `st.button` within `st.columns` for layout in `app.py`.
- [X] T010 [P] [US2] Create operator buttons (+, -, *, /) using `st.button` within `st.columns` in `app.py`.
- [X] T011 [P] [US2] Create parentheses buttons ( ( and ) ) using `st.button` within `st.columns` in `app.py`.
- [X] T012 [US2] Implement logic in the callback to prevent duplicate operator entries (replace last operator) in `app.py`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Clear Functionality (Priority: P1)

**Goal**: The UI provides a 'C' button to clear the current expression and reset the display.

**Independent Test**: Clicking 'C' clears the display and resets the expression.

### Implementation for User Story 3

- [X] T013 [US3] Create the 'C' (Clear) button in `app.py`.
- [X] T014 [US3] Implement logic for 'C' button click to clear `st.session_state.expression` and `st.session_state.result` in `app.py`.

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Evaluate Expression on Equals Button (Priority: P1)

**Goal**: The UI evaluates the current expression using the integrated Python backend when the '=' button is clicked.

**Independent Test**: Clicking '=' evaluates a valid expression and displays the correct result.

### Implementation for User Story 4

- [X] T015 [US4] Create the '=' (Equals) button in `app.py`.
- [X] T016 [US4] Implement logic for '=' button click to call `evaluate_expression(st.session_state.expression)` in `app.py`.
- [X] T017 [US4] Update `st.session_state.result` with the numerical result and `st.session_state.expression` with its string representation in `app.py`.

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Display Error Messages (Priority: P1)

**Goal**: The UI displays clear and concise error messages for invalid expressions or other calculation errors received from the backend.

**Independent Test**: Entering an invalid expression (e.g., "1/0", "1+") displays an appropriate error message.

### Implementation for User Story 5

- [X] T018 [US5] Implement `try-except` block around `evaluate_expression` call to catch `ValueError` and `ZeroDivisionError` in `app.py`.
- [X] T019 [US5] Display caught error messages using `st.error` or similar for user-friendly feedback in `app.py`.

**Checkpoint**: At this point, all user stories should be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T020 [P] Add custom CSS via `st.markdown` to style calculator buttons, display, and layout for a professional look in `app.py`.
- [X] T021 Review `app.py` for PEP 8 compliance, type hints, and docstrings.
- [X] T022 Manually validate the calculator UI against `quickstart.md` scenarios.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Depends on US1 (display must be functional)
- **User Story 3 (P1)**: Depends on US1 (display must be functional)
- **User Story 4 (P1)**: Depends on US1 (display must be functional) and US2 (expression building)
- **User Story 5 (P1)**: Depends on US4 (evaluation must be functional)

### Within Each User Story

- UI components before interaction logic.
- Basic functionality before error handling.
- Story complete before moving to next priority.

### Parallel Opportunities

- All Setup tasks (T001, T002) can run in parallel.
- All Foundational tasks (T003-T006) should be sequential for clarity.
- Within User Story 2, tasks T009-T011 (creating number, operator, parentheses buttons) can run in parallel as they affect different button groups.
- Different user stories generally proceed sequentially due to UI dependencies, but some implementation details might be parallelizable within a story (e.g., styling different button groups).
- Polish tasks T020 (custom CSS) and T021 (code review/docstrings) can run in parallel.

---

## Parallel Example: User Story 2

```bash
# Launch all button creation tasks for User Story 2 together:
- [ ] T009 [P] [US2] Create number buttons (0-9, .) using `st.button` within `st.columns` for layout in `app.py`.
- [ ] T010 [P] [US2] Create operator buttons (+, -, *, /) using `st.button` within `st.columns` in `app.py`.
- [ ] T011 [P] [US2] Create parentheses buttons ( ( and ) ) using `st.button` within `st.columns` in `app.py`.
```

---

## Implementation Strategy

### MVP First (User Story 1, 2, 3, 4, 5 - all core functionality)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. Complete Phase 4: User Story 2
5. Complete Phase 5: User Story 3
6. Complete Phase 6: User Story 4
7. Complete Phase 7: User Story 5
8. **STOP and VALIDATE**: Test all core calculator functionality independently (using `quickstart.md`)
9. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (Display) → Test independently → Deploy/Demo
3. Add User Story 2 (Button Input) → Test independently → Deploy/Demo
4. Add User Story 3 (Clear) → Test independently → Deploy/Demo
5. Add User Story 4 (Evaluate) → Test independently → Deploy/Demo
6. Add User Story 5 (Error Display) → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:
*   Due to the strong UI dependencies, a sequential approach to user stories is generally recommended for a single Streamlit app unless component separation is very strict. However, within certain user stories, button creation can be parallelized.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
```