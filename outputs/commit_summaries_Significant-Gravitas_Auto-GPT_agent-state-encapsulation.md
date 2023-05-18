Commit message: Refactor llm subpackage

Summary:
- Removed `autogpt/core/llm/base.py`
- Renamed `autogpt/core/llm/__init__.py` to `autogpt/core/model/__init__.py`
- Added a new file `autogpt/core/model/base.py` containing base classes Model, ModelInfo, and ModelResponse
- Added a new submodule `autogpt/core/model/embedding`, with a base class EmbeddingModel and related classes EmbeddingModelInfo and EmbeddingModelResponse
- Added a new submodule `autogpt/core/model/language`, with a base class LanguageModel and related classes LanguageModelInfo and LanguageModelResponse
- Created a new empty file `autogpt/core/model/providers/__init__.py`

The commit refactored the llm subpackage by creating separate base classes for Model, EmbeddingModel, and LanguageModel along with their related classes. These new classes were added in their respective subdirectories, and the old `autogpt/core/llm/base.py` file was removed.
---
Commit Summary (2023-05-10): Revise the initial implementation of the plugin manager interface (#4096)

In this commit, James Collins revises the initial implementation of the plugin manager interface to work with the hello world application. Several changes are made:

1. A modification is made in `autogpt/core/plugin/__init__.py`.
2. In `autogpt/core/plugin/base.py`, major changes include:
   - Import modifications and the addition of `PluginType`.
   - `Plugin` is now a union of multiple types.
   - `PluginStorageFormat` and `PluginStorageRoute` classes are introduced.
   - New dataclasses `PluginLocation` and `PluginMetadata` are introduced.
   - The `PluginService` base class is introduced with several abstract methods for loading plugins.
   - The `PluginManager` class has been removed.

These changes involve modifying the plugin system, adding new plugin types and functionalities, and revising the interface for working with plugins. Overall, this commit contributes to improving the plugin manager interface for the application.
---
On May 10, 2023, a commit was made by James Collins with the message "Revise budget manager to work in hello world application (#4040)". In this commit, the `BudgetManager` class was revised, and `ResourceBudget` class was introduced to represent the budget of a particular resource. The changes made include:

1. Refactoring the `BudgetManager` class to be an abstract base class with several abstract methods for managing multiple resource budgets.
2. Introducing a new `ResourceBudget` class as an abstract base class to represent the budget of a particular resource.
3. Adding various abstract methods to the `ResourceBudget` class such as `total_budget`, `total_cost`, `remaining_budget`, `usage`, `update_usage_and_cost`, and `get_resource_budget_prompt`.
4. Updating the `BudgetManager` class with new abstract methods like `list_resources`, `get_total_budget`, `get_total_cost`, `get_remaining_budget`, `get_resource_usage`, `update_resource_usage_and_cost`, and `get_resource_budget_prompt`.

The changes involve 79 additions and 41 deletions, resulting in a total of 120 changes.
---
### Commit Summary (2023-05-10)

- **Commit Author:** Boostrix
- **Commit Message:** Document that Docker Compose 1.29.0 is minimally required (#3963)

This commit updates the project to specify that Docker Compose version 1.29.0 or later is required due to the use of version 3.9 of the Compose file format. The changes include:

1. Comment added in `docker-compose.yml` mentioning the required Docker Compose version.
2. Modifications in `docs/setup.md`:
   - Note about the required Docker Compose version.
   - Instructions to check the installed Docker Compose version.
   - A link to Docker documentation for upgrading Docker Compose if needed.

Co-authored-by: Nicholas Tindle <nick@ntindle.com>
---
On 2023-05-10, Itai Steinherz made a commit to fix the path to the workspace directory in the setup guide. The commit, co-authored by Nicholas Tindle, modifies the `docs/setup.md` file. The change involves updating the volume path in the configuration from `- ./auto_gpt_workspace:/app/auto_gpt_workspace` to `- ./auto_gpt_workspace:/app/autogpt/auto_gpt_workspace`. This change helps correctly map the local workspace directory to the appropriate path in the application.
---
### Commit Summary

**Commit Message:** Re-arch: plugins base (#3995)

**Author:** Nicholas Tindle

**Co-authored-by:** James Collins

This commit focuses on restructuring the architecture of the base plugin system in the Auto-GPT project. The main changes include:

- Added imports for `dataclasses`, `typing`, and `Enum` for more structured code.
- Introduced a `PluginType` Enum with five different plugin types (`COMMAND`, `OPENAPI`, `SYSTEM_REPLACEMENT`, `MESSAGE_SINK`, `LOGGING_SINK`).
- Defined a new dataclass called `Plugin`, which now contains `name`, `description`, `type`, and `plugin_object` attributes.
- Modified the `PluginManager` abstract class to include abstract properties `default_configration`, `__init__`, and `gather_plugins` with proper class annotations and type hints.

This commit enhances the base plugin system's structure, making it more accessible and structured for future integrations.
---
Commit Message: Revise message broker interface (#3986)

In this commit, the message broker interface has been revised with the following changes:

1. Modifications in `autogpt/core/command/base.py`:
   - Import statements have been reorganized.
   - Docstrings have been updated and reformatted.
   - Command class is now properly indented and formatted.

2. Major revisions in `autogpt/core/messaging/base.py`:
   - New abstract interfaces like `MessageEmitter`, `MessageChannel`, and `MessageBroker` have been introduced.
   - Several data classes for message structure like `Sender`, `MessageMetadata`, and `Message` have been added.
   - Some classes have been removed, like `MessageCategory`, `Receiver`, and the old `MessageBroker` class.
   - The new interfaces provide functionality for creating message channels, adding listeners, and emitting messages as well as preserving metadata.
   - There are added methods for importing listeners, sending messages, and managing channels.

Overall, this commit updates and extends the messaging system with new interfaces and data classes, providing more functionality and flexibility for managing messages.
---
On May 8, 2023, Shlomi made a commit to fix a typo in the "getting started" documentation. The commit, co-authored by Richard Beales, modified the 'docs/setup.md' file with 1 addition and 1 deletion. The change made was to the text:
- Original: "It's highly recommended that you keep keep track of your API costs on [the Usage page](https://platform.openai.com/account/usage)."
- Updated: "It's highly recommended that you keep track of your API costs on [the Usage page](https://platform.openai.com/account/usage)."
---
On 2023-05-08, minfeng-ai made a commit to fix typos (#3998) in the Auto-GPT repository, co-authored by Minfeng Lu and Richard Beales. The commit includes four changes:

1. In `autogpt/processing/text.py`, the variable name `flatened_paragraphs` was corrected to `flattened_paragraphs`.
2. In `docs/challenges/introduction.md`, the title of the file was corrected from `indroduction.md` to `introduction.md`.
3. In `tests/integration/goal_oriented/goal_oriented_tasks.md`, the word "successul" was corrected to "successful".
4. In `tests/vcr/vcr_filter.py`, the word "incosistent" was corrected to "inconsistent".
---
#### Commit Summary:
Date: 2023-05-08

Author: Tomasz Kasperczyk

Message: Use correct reference to prompt_generator in autogpt/llm/chat.py (#4011)

Changes: 
- In the file `autogpt/llm/chat.py`, a single line was modified.
- The reference to `prompt_generator` was changed from `agent.prompt_generator` to `agent.config.prompt_generator` within the `chat_with_ai()` function.

This commit fixes the reference to prompt_generator in the chat.py file.
---
Date: 2023-05-08
Author: merwanehamadi
Co-author: xiao.hu <454292663@qq.com>
Commit message: Feature/centralize prompt (#3990)

Summary:
- Added a new file `autogpt/prompts/default_prompts.py` which contains default prompt constants.
- Modified `autogpt/setup.py` to use the default prompt constants from the new file.
- Updated test cassettes in the `tests/integration/cassettes/test_setup/` directory, reflecting the changes in default prompts.

The commit centralizes the default prompts in a separate file, making it easier to manage and modify them in the future.
---
#### Commit Summary

Date: 2023-05-08T02:03:58Z

Author: Kaan

Commit Message: Improve & fix memory challenge docs. (#3989)

Changes:
- In `docs/challenges/memory/challenge_b.md`, the command for running the test is updated from `pytest test/test_memory/test_memory_challenge_b.py::test_memory_challenge_b --level=3` to `pytest -s tests/integration/challenges/memory/test_memory_challenge_b.py --level=3`.
- In `docs/challenges/memory/challenge_c.md`, the command for running the test is updated from `pytest test/test_memory/test_memory_challenge_c.py::test_memory_challenge_c --level=2` to `pytest -s tests/integration/challenges/memory/test_memory_challenge_c.py --level=2`.
---
On 2023-05-08, merwanehamadi made a commit to address the memory challenge C inconsistency (#3985). The commit includes the following changes:

1. Modification in `docs/challenges/memory/challenge_c.md`:
   - Updated the "Status" section: changed the current level to beat from level 2 to level 1.

2. Modification in `tests/integration/challenges/memory/test_memory_challenge_c.py`:
   - Updated the `LEVEL_CURRENTLY_BEATEN` value from 1 to None.
---
#### Commit Summary

Date: 2023-05-07

Author: merwanehamadi

Commit Message: Add code owners policy (#3981)

Summary:
- Added `.github/CODEOWNERS` file
- Specified ownership of the `.github/workflows/` directory to the `@Significant-Gravitas/Auto-GPT-Source` team
---
Title: Command Base Class Interface (#3824)

Author: Daryl Rodrigo

Date: 2023-05-07

Summary: This commit introduces a new `Command` base class representing the actions that an agent can take, along with a `CommandResult` data class for returning the result of a command. The commit also includes a `CommandRegistry` class for managing the registration, retrieval, and execution of command objects, as well as the scanning and loading of command plugins from a specified directory. The `import_commands` method has been implemented to import commands from specified Python modules.
---
## Commit Summary

**Commit**: re-arch: Initial BudgetManager impl (#3919)
**Author**: Richard Beales
**Date**: 2023-05-07

This commit introduces the initial implementation of the `BudgetManager` class, which is an abstract base class for managing constrained resources like a monetary budget, supporting various functionalities like setting, retrieving, and recording costs. Additionally, the commit implements the `BudgetManagerConcrete` class, which extends the `BudgetManager` ABC and provides default configuration values and methods for handling budget operations.
---
Commit Summary (2023-05-07): Initial base.py for message broker agent-state-encapsulation (#3831)

This commit introduces the initial implementation of `base.py` for the message broker. It includes the following changes:

1. Updated imports and added new enums: `MessageCategory` and `Role`.
2. Created `Sender` and `Receiver` classes for handling message senders and receivers.
3. Redesigned the `Message` class as a dataclass and added an abstract base class. It now requires a `sender`, `message`, and `kind_of_message`.
4. Refactored the `MessageBroker` class as an abstract base class with new abstract methods: `broadcast_message`, `get_messages`, `get_listeners`, `register_listener`, and `remove_listener`.
5. Updated type hints and return types for better code readability and maintainability.
---
On 2023-05-07, James Collins made a commit to update docstrings for consistency and conciseness. Changes were made in two files: `autogpt/core/llm/base.py` and `autogpt/core/planning/base.py`. Overall, the commit results in 11 additions and 10 deletions in `base.py`, and 29 additions and 24 deletions in `base.py`. The modifications mostly involve rephrasing descriptions, improving formatting and removing redundant type indications in the docstrings.
---
#### Commit Summary:

The commit introduces a new logging interface in the Auto-GPT project. The key changes include:

1. Added `LogFormat` Enum with values: NONE, MARKDOWN, JSON, TEXT, and YAML.
2. Added `LogMessage` dataclass containing title, message, format, and metadata.
3. Added `LogLevels` Enum with values: NONE, ERROR, WARN, INFO, DEBUG, and SILLY.
4. Modified the base `Logger` class to include abstract methods for initialization, debug, info, warn, error, and setting the log level.
---
Commit Summary (Date: 2023-05-07, Author: James Collins):
Add language model base and work out interactions with planning manager (#3850)

The commit modifies three files: 'autogpt/core/configuration/base.py', 'autogpt/core/llm/base.py' and 'autogpt/core/planning/base.py'. Changes include the addition of LanguageModel class, creation of several dataclasses (ModelInfo, ChatModelInfo, EmbeddingModelInfo, etc.) and refactoring of PlanningManager with new classes and methods. The goal is to improve the interactions between the planning manager and the language model base.
---
On May 6, 2023, merwanehamadi made a commit titled "add information retrieval challenge to the wiki (#3876)". The commit adds two new files: 'docs/challenges/information_retrieval/challenge_a.md' and 'docs/challenges/information_retrieval/introduction.md'. The 'challenge_a.md' file describes the Information Retrieval Challenge A, where the agent's objective is to find the revenue of Tesla in 2022 and write the result in 'output.txt'. The 'introduction.md' file offers a brief overview of Information Retrieval challenges, which evaluate an AI agent's ability to search, extract, and present relevant information from various sources. Additionally, the commit modifies 'mkdocs.yml' to include the new Information Retrieval section, comprising the introduction and Challenge A pages in the navigation.
---
### Commit Summary

**Commit Title**: Implement Logging of User Input in logs/Debug Folder (#3867)

**Commit Date**: 2023-05-06

**Commit Author**: Andres Caicedo

**Description**: This commit adds logging of user input to the `logs/Debug` folder and introduces the following changes:

1. A new constant `USER_INPUT_FILE_NAME` is added in `autogpt/log_cycle/log_cycle.py`.
2. The method `start_interaction_loop()` in `autogpt/agent/agent.py` is updated to log user input when `console_input` is not the `authorise_key`.
---
On 2023-05-05, Pi made a commit titled "Add link to wiki page on Contributing." In this commit, the `.github/ISSUE_TEMPLATE/2.feature.yml` file was modified. The changes included:

- Updating the description text for a feature request.
- Adding a link to the Contributing wiki page.
- Adjusting the format and removing a redundant line ("Thanks for contributing by creating an issue! ❤️").

In total, there were 3 additions and 4 deletions, resulting in 7 overall changes to the file.
---
Date: 2023-05-05T22:07:55Z

Author: Pi

Commit Message: "fix"

Summary:

In this commit, a minor modification was made to the `.github/ISSUE_TEMPLATE/1.bug.yml` file. A syntax error in the Markdown link formatting was corrected.

Changes Made:
- Fixed link formatting for the "wiki page on Contributing" in the 1.bug.yml issue template.

The diff included 1 addition and 1 deletion, resulting in 2 changes overall.
---
On May 5, 2023, Pi made a commit with the message "Add link to wiki Contributing page." In this commit, a link to the Contributing wiki page was added to the .github/ISSUE_TEMPLATE/1.bug.yml file. This addition aims to help users find and read the contributing guidelines before filing a new issue. The change involved 2 lines of additions and no deletions.
---
On 2023-05-05, Pi committed an update to the PULL_REQUEST_TEMPLATE.md file. The change involved adding a link to the Auto-GPT project's wiki page on contributing. This aims to provide better guidance for contributors, potentially leading to quicker merges after testing. The commit's SHA is `273275b30b7ffb577d5fa344a67a0c929277d8d5`.
---
On 2023-05-05, Pi made a commit titled "Update README.md." In this commit, Pi modified the README.md file and added a new line suggesting users check out the project's wiki. The commit had 1 addition and 0 deletions, making a total of 1 change in the README.md file.
---
On 2023-05-05, merwanehamadi made a commit titled "community challenges in the wiki (#3764)". This commit adds several new files and updates the MkDocs configuration file. The new files introduce the concept of challenges for the Auto-GPT project, including guidelines for submitting and beating challenges, a list of challenges, and detailed descriptions of specific memory challenges. The MkDocs configuration file has been updated to include this new content in the documentation navigation structure.
---
