# Tasks: Basic Calculator Operations

**Input**: Design documents from `/specs/001-calc-ops/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/api.md, research.md, quickstart.md

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Initialize Python project with `uv` (e.g., `uv init`) to create `pyproject.toml`
- [ ] T002 Create project directory `src/calculator/`
- [ ] T003 Create `src/calculator/__init__.py`
- [ ] T004 Create `tests/unit/` and `tests/integration/` directories
- [ ] T005 Configure `pytest` for test discovery and execution

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 Create `src/calculator/utils.py` for float comparison utility (e.g., `is_close` function with configurable epsilon)

---

## Phase 3: User Story 1 - Add Two Numbers (Priority: P1) 🎯 MVP

**Goal**: Implement and test the addition operation.

**Independent Test**: Verify `add` function works correctly for various numeric inputs, including positive, negative, zero, and decimals.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T007 [P] [US1] Create `tests/unit/test_operations.py`
- [ ] T008 [P] [US1] Add unit tests for `add` function in `tests/unit/test_operations.py`

### Implementation for User Story 1

- [ ] T009 [US1] Implement `add` function in `src/calculator/operations.py`

---

## Phase 4: User Story 2 - Subtract Two Numbers (Priority: P1)

**Goal**: Implement and test the subtraction operation.

**Independent Test**: Verify `subtract` function works correctly for various numeric inputs, including positive, negative, zero, and decimals.

### Tests for User Story 2 ⚠️

- [ ] T010 [P] [US2] Add unit tests for `subtract` function in `tests/unit/test_operations.py`

### Implementation for User Story 2

- [ ] T011 [US2] Implement `subtract` function in `src/calculator/operations.py`

---

## Phase 5: User Story 3 - Multiply Two Numbers (Priority: P1)

**Goal**: Implement and test the multiplication operation.

**Independent Test**: Verify `multiply` function works correctly for various numeric inputs, including positive, negative, zero, and decimals.

### Tests for User Story 3 ⚠️

- [ ] T012 [P] [US3] Add unit tests for `multiply` function in `tests/unit/test_operations.py`

### Implementation for User Story 3

- [ ] T013 [US3] Implement `multiply` function in `src/calculator/operations.py`

---

## Phase 6: User Story 4 - Divide Two Numbers (Priority: P1)

**Goal**: Implement and test the division operation, including division by zero handling.

**Independent Test**: Verify `divide` function works correctly for various numeric inputs and returns the specified error message for division by zero.

### Tests for User Story 4 ⚠️

- [ ] T014 [P] [US4] Add unit tests for `divide` function in `tests/unit/test_operations.py`

### Implementation for User Story 4

- [ ] T015 [US4] Implement `divide` function in `src/calculator/operations.py`

---

## Phase 7: Additional Operations (Priority: P1)

**Goal**: Implement and test remaining mathematical operations.

**Independent Test**: Each operation can be tested independently for correctness.

### Tests for Additional Operations ⚠️

- [ ] T016 [P] [US_ADD] Add unit tests for `power` function in `tests/unit/test_operations.py`
- [ ] T017 [P] [US_ADD] Add unit tests for `modulo` function in `tests/unit/test_operations.py`
- [ ] T018 [P] [US_ADD] Add unit tests for `sqrt` function in `tests/unit/test_operations.py`
- [ ] T019 [P] [US_ADD] Add unit tests for `log` and `ln` functions in `tests/unit/test_operations.py`
- [ ] T020 [P] [US_ADD] Add unit tests for `sin`, `cos`, `tan` functions in `tests/unit/test_operations.py`
- [ ] T021 [P] [US_ADD] Add unit tests for `factorial` function in `tests/unit/test_operations.py`

### Implementation for Additional Operations

- [ ] T022 [US_ADD] Implement `power` function in `src/calculator/operations.py`
- [ ] T023 [US_ADD] Implement `modulo` function in `src/calculator/operations.py`
- [ ] T024 [US_ADD] Implement `sqrt` function in `src/calculator/operations.py`
- [ ] T025 [US_ADD] Implement `log` and `ln` functions in `src/calculator/operations.py`
- [ ] T026 [US_ADD] Implement `sin`, `cos`, `tan` functions in `src/calculator/operations.py`
- [ ] T027 [US_ADD] Implement `factorial` function in `src/calculator/operations.py`

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T028 Ensure 100% test coverage for `src/calculator/operations.py`
- [ ] T029 Run `mypy` for type checking across `src/calculator/`
- [ ] T030 Review `src/calculator/` code against constitution rules (PEP 8, docstrings, magic numbers, line length)
- [ ] T031 Update `quickstart.md` with final usage examples for all implemented operations

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

- All user stories (Phase 3-7) can start after Foundational (Phase 2) and are largely independent of each other.

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Implementation of functions

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Implementation tasks for different operations can be done in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Two Numbers)
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add Additional Operations → Test independently → Deploy/Demo

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Add)
   - Developer B: User Story 2 (Subtract)
   - Developer C: User Story 3 (Multiply)
   - Developer D: User Story 4 (Divide)
   - Developer E: Additional Operations (e.g., Power, Modulo)
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
