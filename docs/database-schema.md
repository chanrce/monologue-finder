# Database Schema

## Monologues

| Field | Type | Description |
|---|---|---|
| id | integer | Unique identifier for the monologue |
| play | string | Title of the play |
| character | string | Character performing the monologue |
| playwright | string | Author of the play |
| genre | string | Genre of the play |
| gender | string | Gender of the character |
| age_range | string | Typical casting age range |
| era | string | Era/category, such as Classical or Contemporary |
| tone | multiple values | Tones associated with the monologue, such as comedic, angry, romantic, or grieving |
| word_count | integer | Number of words in the monologue |
| text | text | Full text of the monologue |
| act | integer | Act in which the monologue appears |
| scene | integer | Scene in which the monologue appears |
| opening_line | string | Opening line used to identify the monologue |

## Derived Values

The application can generate values that do not need to be stored separately:

- **Display label:** generated from `play` and `character` (for example, `Cymbeline — Imogen`)
- **Length bucket:** generated from `word_count` (for example, Short, Medium, or Long)