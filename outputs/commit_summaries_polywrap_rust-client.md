On May 10th, 2023 at 21:59:11 UTC, Jure Bogunovic removed unnecessary test prefixes from test functions in two files (`test_env_with_invoke.rs` and `test_env_with_subinvoke.rs`). The changes included renaming the functions to remove the `test_` prefix and changing the `should_panic` test function names. The commit contained a diff with a total of 14 line changes and 7 additions/deletions in each file.
---
On 2023-05-10T20:45:02Z, Jure Bogunovic pushed a commit that fixed an issue with empty environment serialization not being empty. They modified the `wasm_wrapper.rs` file in the `packages/wasm/src` directory, changing the serialization of an empty environment from `msgpack!({})` to `vec![]`. This change will ensure that an empty environment is properly serialized as empty.
---
This commit updated the version of the wrap test harness from "0.0.1-pre.5" to "0.1.1" in the file "packages/tests-utils/src/bin/generate.rs".
---
On 2023-05-10, Cesar merged the 'main' branch into nerfzael-env-tests-and-fixes. The commit updated the versions of various packages and dependencies, including polywrap_client, polywrap_wasm, polywrap_client_builder, polywrap_core, wrap_manifest_schemas, polywrap_resolvers, polywrap_msgpack, polywrap_tests_utils, and polywrap_plugin_implementor. The commit also updated the VERSION file and modified several files in the packages/default-config directory to use updated dependencies.
---
On 2023-05-10T16:39:04Z, the `polywrap-build-bot` made a commit with a message of `0.1.6-beta.2 (#87)`. The commit updated the versions of multiple dependencies in the `Cargo.toml` file and the `polywrap_client_default_config` package.
---
This commit made by Cesar Brazon updated the version of the project to 0.1.6-beta.2 by modifying the VERSION file. The diff shows that version 0.1.6-beta.1 was replaced with version 0.1.6-beta.2 in the VERSION file.
---
On May 10 2023, Cesar Brazon removed `polywrap_client` as the only dependency in `packages/default-config/Cargo.toml` and added dependencies to `polywrap_core`, `polywrap_plugin`, `polywrap_client_builder`, `polywrap_msgpack`, and `wrap_manifest_schemas`. This commit also modified imports in `packages/default-config/src/embeds/` to address the dependency changes and updated `polywrap_client::builder::types::BuilderConfig` to `polywrap_client_builder::types::BuilderConfig` in `packages/default-config/src/lib.rs`. The total changes implemented in this commit is 12 additions and 16 deletions.
---
On 2023-05-09T18:45:34Z, Jure Bogunovic removed whitespace from two test files in the "packages/client/tests" directory. The first file had two lines removed and the second file had one line removed.
---
Jure Bogunovic made a commit on May 9th, 2023 at 18:41:46 UTC with the message "moved method to top". The commit modified a file named "test_env_with_invoke.rs" and contained a diff with 26 changes (13 additions and 13 deletions). The changes involved moving a method named "get_env_wrapper_uri()" to the top of the file and removing its original location. The file appears to be related to a Rust client, specifically to test environment variables in an integration test.
---
Sure! On 2023-05-08T15:40:48Z, namesty made a commit with the message "added invoke_wrapper_raw back into Client trait". The commit modified multiple files and added a new function called `invoke_wrapper_raw` to the `Client` trait. The function takes in certain parameters, performs some operations, and returns a `Result<Vec<u8>, Error>`. Some code has been modified in the `FFIInvoker` and `FFIClient` structures to use this new function.
---
Sure! On 2023-05-07T14:44:23Z, namesty made a commit with the message "added load_wrapper to client trait". In this commit, they modified the `Client` trait in `packages/core/src/client.rs`, adding a new method called `load_wrapper`. This method takes a URI and an optional `UriResolutionContext` parameter, and returns a result containing an `Arc` to a dynamic trait object (`dyn Wrapper`) or an error of type `Error`. The commit added 10 lines of code and removed 1 line, for a total of 10 changes.
---
On 2023-05-05T23:04:01Z, `namesty` made a commit titled `(chore): eliminated invoke_wrapper from Invoker` in the `packages/core/src/invoke.rs` file. The commit removed the `invoke_wrapper_raw` method from the `Invoker` trait and made some adjustments to the file. The commit had 1 addition and 11 deletions, for a total of 12 changes.
---
Jure Bogunovic made a commit on 2023-05-05T16:44:20Z which added a missing import in the `test_env_with_invoke.rs` file. The commit added `use polywrap_tests_utils::helpers::get_tests_path` to the existing imports in the file. The diff for this commit shows an addition of 1 line of code to the file.
---
Jure Bogunovic removed an old test called "test_env.rs" which was no longer needed. The test file had 117 lines of code, and there were no other changes to the codebase.
---
Jure Bogunovic added a new test for the resolution path environment in the `test_env_with_invoke.rs` file. The new test `test_env_can_be_registered_for_any_uri_in_resolution_path()` is currently commented out as it requires the `getEnvFromUriHistory` feature to be implemented and has an associated Issue #79 on GitHub.
---
On 2023-05-05T14:00:19Z, Nestor Amesty merged a pull request (#78) that addressed an issue with encoding empty arguments in the Rust client for Polywrap. The commit modified the `wrapper.rs` and `wasm_wrapper.rs` files and added the `polywrap_msgpack::msgpack()` function to encode empty arguments as an empty MessagePack object.
---
On 2023-05-05T13:59:58Z, namesty removed temporarily the test_no_args.rs file in the `packages/client/tests/` directory. The commit removed 50 lines of code that included a test that invoked a method with no arguments and checked if the result was true.
---
The commit titled "(fix): test map_type" by namesty made a change to a Rust file in the "packages/client/tests" directory. Specifically, they fixed a typo in the naming of a field in the "CustomMap" struct. The diff shows that they changed the field "nested_map" to "nestedMap" in the struct definition and also in its usage in the test function "map_type_test".
---
On 2023-05-05T13:52:54Z, namesty made a commit that changed uri.uri to uri.to_string() in multiple files, specifically in client_config_builder.rs, test_builder.rs, client.rs, helpers.rs, uri.rs, and uri_resolver_wrapper.rs. The changes were made to improve the code and fix errors related to URI resolution.
---
The commit made by namesty on 2023-05-05T01:05:33Z with the message "(chore): fix for test_map_type" is a modification to the 'test_map_type.rs' file in the 'client/tests' directory. The changes made include renaming a variable 'foobar' to 'foo' and updating its usage in the code. The PR has 3 additions and 3 deletions, resulting in a total of 6 changes.
---
On 2023-05-05, namesty made a commit with the message "fix: plugin invocation test". They modified the test_plugin_invocation.rs file to import and use additional modules. They also made changes to the following files: native/src/lib.rs and plugin/implementor/src/lib.rs.
---
