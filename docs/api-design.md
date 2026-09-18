GET /monologues

If no search or filters are provided:
- Return 10 random monologues for inspiration when no search or filters are provided.
- Each result includes basic monologue details and a way to access the full monologue.

### Purpose

Retrieves monologues according to user search parameters and/or selected filters.

### Search Parameters

A general search input can be used for text-based searches such as playwright, play, character.

### Query Parameters

- Playwright
- Title
- Character
- Era
- Genre
- Gender
- Age_range
- Tone


### Response

Returns a list of matching monologues.

Each result should include basic information such as:

- Monologue_id
- Title
- Character
- Playwright
- Era
- Genre
- Tone
- Word_count
- Opening_line

---

## GET /monologues/{id}

### Purpose

Retrieves specific monologue by its ID, including the full monologue text and information such as playwright, character, play title, tone, and length.

### Response

Returns the selected monologue including:

- Monologue_id
- Text
- Character
- Title
- Playwright
- Act
- Scene
- Genre
- Era
- Tone
- Age_range
- Gender
- Word_count

### Errors

- 404 Not Found: returned when the requested Monologue_id does not exist.

### Path Parameters

- id (integer) — the Monologue_id of the monologue being requested.