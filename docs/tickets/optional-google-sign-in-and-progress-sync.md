# Optional Google sign-in and cross-device progress sync

**Status:** To complete design and implement  
**Created:** 16 September 2026  
**Scope:** Shared application engine; DCIT418 is the current reference implementation  
**Implementation:** Not started

## Outcome

Let students optionally sign in with Google to automatically synchronize their learning progress across devices. The app must remain fully usable without an account, with local progress and offline study. Sign-in must never block access to practice or revision.

This ticket records the proposed feature. Firebase and the model below are candidates for the design, not configured infrastructure or completed functionality.

## Proposed experience

- Offer a small **Sign in with Google to sync** action with a clear explanation of what will be uploaded.
- On first sign-in, offer to merge existing guest progress into the account without silently replacing either history.
- Restore account progress when signing in on another device.
- Save changes locally while offline and synchronize when connectivity returns.
- Display meaningful states: local only, syncing, synced, offline with changes pending, and sync failed with retry.
- Support sign-out and account switching with isolated local data for each account and the guest.
- Keep JSON import/export available for backups and manual transfer.
- Preserve existing mock deadlines when resuming on another device.

## Candidate architecture

Use Firebase Authentication for Google sign-in and Cloud Firestore for account-scoped progress. Keep the synchronization layer separate from grading, sampling and the UI so it can be reused across course adaptations or replaced later.

Current integration points:

- [`src/model.ts`](../../src/model.ts): `Progress`, `Attempt`, `Session`, `Draft`, grading and progress validation.
- [`src/main.tsx`](../../src/main.tsx): local persistence, preferences, progress import/export and session interactions.

Current `Progress` contains a course marker, schema version, attempts, seen IDs and one active session. Preferences are stored separately. The existing local model is a starting point, not a conflict-safe cloud protocol.

## Proposed data model

```text
users/{userId}
  preferences/{setting}
  courses/{courseId}
    banks/{bankVersion}
      attempts/{attemptId}
      seen/{questionId}
      sessions/{sessionId}
        drafts/{questionId}
```

| Record | Candidate fields | Purpose |
|---|---|---|
| User | Auth user ID, schema version, created time | Account boundary; avoid duplicating unnecessary profile data |
| Preference | Setting name, value, update time/revision | Theme, font size and agreed preferences |
| Course/bank | Course ID, bank version, schema version | Isolate course content and question identities |
| Attempt | ID, question ID, session ID, answer, correctness, seconds, mode, timestamp, override, revision | Preserve submitted answers and manual corrections |
| Seen | Question ID, first-seen time | Combine exposure from reading and answering |
| Session | ID, mode, ordered question IDs, option orders, cursor, start time, deadline, status, revision, editing device | Resume practice or generated mocks |
| Draft | Question ID, answer text, selected option(s), accumulated seconds, revision | Restore in-progress answers |

Use stable unique IDs for writes so retries and repeated imports are idempotent. Distinguish client event times from server acknowledgement times. Course IDs and bank versions must be validated rather than accepted as arbitrary mappings to current questions.

The parser can currently reassign question IDs. Design stable question identity and explicit bank-version migration before enabling cross-version progress reuse. A schema version alone does not identify a question-bank version.

Calculate accuracy, mistake lists and mock-history summaries from attempts. Do not maintain independent authoritative counters that can drift. Sync progress references and user responses; uploading the bundled question bank or study documents is outside this feature.

## Merge and conflict requirements

- **Attempts:** Merge by stable attempt ID; repeated delivery must not create duplicate attempts. Define how imported legacy IDs are preserved or mapped.
- **Seen records:** Union exposure across devices, preserving a consistent first-seen value.
- **Preferences:** Resolve changes per setting using an explicit ordering rule; do not overwrite unrelated settings.
- **Overrides:** Treat correctness overrides as versioned updates to an existing attempt, not new attempts.
- **Sessions:** Design explicit handover and revision checks. Two devices must not silently overwrite the same active paper or its drafts.
- **Offline session conflicts:** Preserve conflicting work until reconciled. Decide how resumed sessions, duplicate submission, expired papers and elapsed time are resolved.
- **Deletion/reset:** Define deletion markers or a reset generation so an old offline device cannot restore progress the user deliberately deleted.

Firestore's default last-write-wins behavior is not sufficient for active mock conflict resolution. Transaction-based designs must account for transactions requiring connectivity. Do not promise exclusive editing across disconnected devices without a reconciliation policy.

## Design decisions still required

- [ ] Confirm Firebase Authentication and Firestore, ownership of the project, hosting domains and environment setup.
- [ ] Define mobile/desktop sign-in flow, cancellation and blocked-popup/redirect handling.
- [ ] Finalize schema, stable question IDs, bank migration and backward-compatible JSON import/export.
- [ ] Define first-sign-in merge consent, repeated import handling and guest/account storage boundaries.
- [ ] Define session ownership, handover, offline conflicts, submission and timeout behavior.
- [ ] Decide which preferences and reading state sync; the current reading cursor is not persisted.
- [ ] Define sync batching, retry/backoff, write frequency, pending-write storage and cost controls.
- [ ] Define progress reset, account/cloud-data deletion and cache cleanup on shared devices.
- [ ] Specify per-user database rules, field validation and allowed updates, including protection against another user's reads/writes.
- [ ] Specify user-facing data-use text and minimum stored account information.
- [ ] Confirm the owner-designated main app repository for shared engine contributions; its URL/contact details are still forthcoming.

## Implementation checklist

- [ ] Complete and record the design decisions above.
- [ ] Add environment configuration and setup documentation without committing credentials or service-account secrets.
- [ ] Implement optional authentication and account-aware local storage.
- [ ] Implement the cloud repository, migrations, merge rules and offline synchronization.
- [ ] Add minimal sign-in, account, sync-status and conflict-resolution UI.
- [ ] Implement and test Firestore security rules before enabling live writes.
- [ ] Add meaningful model, emulator and browser tests for synchronization and account isolation.
- [ ] Validate Google sign-in and two-device synchronization against configured infrastructure.
- [ ] Update the feature inventory and user documentation only after verified implementation.

## Acceptance criteria

- [ ] A guest can use all current study modes without signing in or contacting the sync service.
- [ ] Declining or cancelling sign-in leaves guest progress intact.
- [ ] First-sign-in merge preserves existing local and cloud attempts without duplicates.
- [ ] Attempts, seen questions, mock history and selected preferences appear on a second signed-in device.
- [ ] Offline changes survive reload and synchronize after reconnecting.
- [ ] Account switching cannot expose or upload the previous account's progress into another account.
- [ ] Different courses and incompatible bank versions cannot mix question progress.
- [ ] Conflicting active-session edits are preserved and resolved explicitly; a mock deadline never restarts on handover.
- [ ] Retried writes and repeated mock submissions do not duplicate results.
- [ ] Reset/deletion is not reversed by an outdated offline device.
- [ ] Unauthorized cross-user reads and writes fail in security-rule tests.
- [ ] Sync status reflects pending/failed writes accurately, and errors do not prevent local study.
- [ ] Existing practice, reading, grading, offline caching and JSON backup behavior pass regression checks.

## Design references

- [Google sign-in with Firebase](https://firebase.google.com/docs/auth/web/google-signin)
- [Firestore data model](https://firebase.google.com/docs/firestore/data-model)
- [Offline persistence and conflict behavior](https://firebase.google.com/docs/firestore/manage-data/enable-offline)
- [Transactions and batched writes](https://firebase.google.com/docs/firestore/manage-data/transactions)
- [User-scoped Firestore security rules](https://firebase.google.com/docs/firestore/security/rules-conditions)
