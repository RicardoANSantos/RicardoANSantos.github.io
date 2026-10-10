# Updating the website with an AI assistant

The website's files are the durable context. The AI edits them when you request an
update; GitHub automatically publishes successful changes pushed to `main`.
There is no AI service running inside the public website and no API key is needed
for the website's build or hosting.

## First connection

1. Publish the repository using `SETUP.md`.
2. Give the GitHub plugin or Codex environment access to
   `RicardoANSantos/RicardoANSantos.github.io`. If access is limited to selected
   repositories, add the new repository after creating it.
3. In future requests, provide the repository link and ask the assistant to read `AGENTS.md`.

## Example requests

**New paper:**

> Update my website at https://github.com/RicardoANSantos/RicardoANSantos.github.io.
> Read AGENTS.md. This paper is now published: [DOI or attached paper]. Update its
> status, write a short research summary, and publish the checked changes.

**New CV:**

> Replace my website's downloadable CV with the attached version. Update my online
> CV, biography, affiliation, contact details, and publication list wherever the new
> CV changes them. Publish the checked changes.

**New photo:**

> Add these photos to the website. They show [activity/location] on [date]. Choose
> the best images, write concise captions and alt text, and publish the update.

**Draft first:**

> Prepare an update from this material and show me a preview before publishing.

## What is automatic

- Formatting, edits, consistency checks, and link checks can be handled by the assistant.
- GitHub builds and publishes once an authorized change reaches `main`.
- Merely uploading a file to a chat does not publish it. Include an update instruction.
- A folder-watching or unattended upload-to-publication agent would be a separate
  integration; it is not configured in this initial version.

## Reverting a change

Ask the assistant to revert the relevant Git commit. Once that reversal is pushed
to `main`, GitHub republishes the previous content. Avoid restoring files from an
old ZIP when Git history is available.
