# Database Schema

## Playwright Table

| Field | Type | Key | Description |
|---|---|---|---|
| Playwright_id | integer | PK | Unique identifier for the playwright |
| Name | string |  | Playwright name |

Relationship:

One Playwright → many Play rows

`Play.Playwright_id (FK)` references `Playwright.Playwright_id (PK)`

---

## Play Table

| Field | Type | Key | Description |
|---|---|---|---|
| Play_id | integer | PK | Unique identifier for play |
| Playwright_id | integer | FK | References playwright who wrote the play |
| Title | string |  | Play Title |
| Era | string |  | Era/category, eg Classical or Contemporary |
| Genre | string |  | Genre of the play |

Relationship:

One Play → many Character rows

`Character.Play_id (FK)` references `Play.Play_id (PK)`

---

## Character Table

| Field | Type | Key | Description |
|---|---|---|---|
| Character_id | integer | PK | Unique identifier for the character |
| Play_id | integer | FK | References the play the character belongs to |
| Character | string |  | Character name |
| Gender | string |  | Character gender |
| Age_range | string |  | Typical casting age range |

Relationship:

One Character → many Monologue rows

`Monologue.Character_id (FK)` references `Character.Character_id (PK)`

---

## Monologue Table

| Field | Type | Key | Description |
|---|---|---|---|
| Monologue_id | integer | PK | Unique identifier for the monologue |
| Character_id | integer | FK | References the character performing the monologue |
| Text | text |  | Full text of the monologue |
| Act | integer |  | Act in which the monologue appears |
| Scene | integer |  | Scene in which the monologue appears |
| Opening_line | string |  | Opening line used to identify the monologue |
| Word_count | integer |  | Number of words in the monologue |

---

## Tone Table

| Field | Type | Key | Description |
|---|---|---|---|
| Tone_id | integer | PK | Unique identifier for the tone |
| Tone | string |  | Tone value, such as comedic, angry, romantic, or grieving |

---

## Monologue_Tone Table

| Field | Type | Key | Description |
|---|---|---|---|
| Monologue_id | integer | FK | References a monologue |
| Tone_id | integer | FK | References a tone |

Relationship:

Many Monologues ↔ many Tones

The `Monologue_Tone` table connects monologues and tones.

---

## Derived Values

The application can generate values that do not need to be stored separately:

- **Display label:** generated from `Title` and `Character`
  - Example: `Cymbeline — Imogen`

- **Length bucket:** generated from `Word_count`
  - Example: Short, Medium, or Long