# Project notes for the factory

## Product
CardVault is a self-hosted app for scanning trading cards (sports, Pokémon, Magic, Yu-Gi-Oh!), tracking where each is stored, pricing them against eBay and listing them for sale.

## Security hot spots
The FastAPI routers in `backend/app` (single-user app, but check any new endpoint's input validation); uploaded card photos (file names, paths, size and type; served from `/images`); eBay and Anthropic API keys and OAuth tokens (never logged, never returned to the browser, never committed); user-edited search strings and card fields that reach eBay queries or SQLModel queries; text rendered in the Vue frontend (`v-html`); and `.env`, `*.db` and `backend/data/`, which must never be committed.

## UI conventions
The Vuetify theme and defaults are configured in `frontend/` (Nuxt plugins and `nuxt.config.ts`); shared components live in `frontend/components/`. Prefer Vuetify components and theme colours over custom CSS.

## Users
A card collector or reseller, usually on a phone while scanning a stack of cards and filing them into binders and boxes. Speed of repeated actions, clear prices and their basis (sold, asking or manual), and no lost work in the scan queue matter most.

## Always escalate
Changes to how card values or prices are calculated or labelled; eBay listing or publishing (it spends the user's real account); SQLite models or data-migration code; how API keys and `.env` are read.
