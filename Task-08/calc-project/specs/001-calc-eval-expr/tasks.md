# Tasks: 001-calc-eval-expr

**Input**: Design documents from `/specs/001-calc-eval-expr/`
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

- [X] T001 Create `src/calculator/evaluation.py` for expression evaluation logic.
- [X] T002 Create `tests/unit/test_evaluation.py` for unit tests of expression evaluation.
- [X] T003 Configure Python environment for new module and tests (e.g., update `__init__.py` if necessary).

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Define token types (e.g., Number, Operator, Parenthesis) in `src/calculator/evaluation.py`.
- [X] T005 Implement a tokenizer/lexer to convert expression string into tokens in `src/calculator/evaluation.py`.
- [X] T006 Define Abstract Syntax Tree (AST) node classes (e.g., NumberNode, BinaryOperationNode) in `src/calculator/evaluation.py`.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Evaluate Valid Arithmetic Expression (Priority: P1) 🎯 MVP

**Goal**: To enable the calculator to evaluate valid arithmetic expressions, support basic arithmetic operations, and adhere to standard mathematical order of operations.

**Independent Test**: Given a valid arithmetic expression string, `evaluate_expression` returns the correct floating-point result according to PEMDAS/BODMAS.

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T007 [P] [US1] Write unit tests for basic arithmetic operations (addition, subtraction) in `tests/unit/test_evaluation.py`.
- [X] T008 [P] [US1] Write unit tests for multiplication and division operations in `tests/unit/test_evaluation.py`.
- [X] T009 [P] [US1] Write unit tests for order of operations (PEMDAS/BODMAS) without parentheses in `tests/unit/test_evaluation.py`.
- [X] T010 [P] [US1] Write unit tests for expressions involving parentheses in `tests/unit/test_evaluation.py`.
- [X] T011 [P] [US1] Write unit tests for floating-point number evaluation in `tests/unit/test_evaluation.py`.

### Implementation for User Story 1

- [X] T012 [US1] Implement a parser to convert tokens into an AST in `src/calculator/evaluation.py` (focus on valid syntax).
- [X] T013 [US1] Implement an AST evaluator to compute the result from the AST in `src/calculator/evaluation.py`.
- [X] T014 [US1] Integrate tokenizer, parser, and evaluator into the `evaluate_expression` function signature in `src/calculator/evaluation.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Detect Invalid Expressions (Priority: P1)

**Goal**: To gracefully handle invalid expressions by detecting and reporting errors.

**Independent Test**: Given an invalid arithmetic expression string, `evaluate_expression` raises the appropriate `ValueError` or `ZeroDivisionError` with a descriptive message.

### Tests for User Story 2

- [X] T015 [P] [US2] Write unit tests for invalid syntax (e.g., mismatched parentheses, incomplete expressions) in `tests/unit/test_evaluation.py`.
- [X] T016 [P] [US2] Write unit tests for unsupported characters in `tests/unit/test_evaluation.py`.
- [X] T017 [P] [US2] Write unit tests for division by zero errors in `tests/unit/test_evaluation.py`.
- [X] T018 [P] [US2] Write unit tests for empty expression string in `tests/unit/test_evaluation.py`.

### Implementation for User Story 2

- [X] T019 [US2] Enhance tokenizer to detect and raise `ValueError` for unsupported characters in `src/calculator/evaluation.py`.
- [X] T020 [US2] Enhance parser to detect and raise `ValueError` for syntax errors (e.g., mismatched parentheses, unexpected tokens) in `src/calculator/evaluation.py`.
- [X] T021 [US2] Enhance evaluator to detect and raise `ZeroDivisionError` for division by zero scenarios in `src/calculator/evaluation.py`.
- [X] T022 [US2] Ensure `evaluate_expression` correctly propagates `ValueError` and `ZeroDivisionError` as per contract in `src/calculator/evaluation.py`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T023 Add comprehensive docstrings to functions and classes in `src/calculator/evaluation.py`.
- [X] T024 Add type hints to all function parameters and return values in `src/calculator/evaluation.py`.
- [X] T025 Ensure PEP 8 compliance and apply formatting (e.g., `ruff format`) to `src/calculator/evaluation.py` and `tests/unit/test_evaluation.py`.
- [X] T026 Review code for potential optimizations and refactoring in `src/calculator/evaluation.py`.
- [X] T027 Run `pytest --cov=src/calculator/evaluation` to ensure high code coverage for the evaluation module.

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
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Models before services (N/A here, but token types and AST nodes should be defined before parser/evaluator)
- Services before endpoints (N/A here, but tokenizer/parser/evaluator before `evaluate_expression` integration)
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T001, T002, T003 - though in this case T001 and T002 are file creations, T003 is configuration).
- All Foundational tasks (T004, T005, T006) should be sequential for clarity of implementation, though some minor parts could be parallel.
- Once Foundational phase completes, User Stories 1 and 2 can be worked on in parallel by different team members.
- All tests for a user story marked [P] can run in parallel (e.g., T007-T011, T015-T018).
- Implementation tasks within a story can be sequential.
- Polish tasks marked [P] can run in parallel.

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
- [ ] T007 [P] [US1] Write unit tests for basic arithmetic operations (addition, subtraction) in `tests/unit/test_evaluation.py`.
- [ ] T008 [P] [US1] Write unit tests for multiplication and division operations in `tests/unit/test_evaluation.py`.
- [ ] T009 [P] [US1] Write unit tests for order of operations (PEMDAS/BODMAS) without parentheses in `tests/unit/test_evaluation.py`.
- [ ] T010 [P] [US1] Write unit tests for expressions involving parentheses in `tests/unit/test_evaluation.py`.
- [ ] T011 [P] [US1] Write unit tests for floating-point number evaluation in `tests/unit/test_evaluation.py`.
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
