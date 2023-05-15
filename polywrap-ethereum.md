-> **Question**: Create a sample call to the ethereum wrapper using the polywrap python client. 

**Answer**: Here is an example call to a Ethereum wrapper using the Polywrap Python Client:

```python
from polywrap_core import Uri, InvokerOptions, PolywrapClient

async def call_ethereum_wrapper():
    # Instantiate the client
    client = PolywrapClient()

    # Load the Ethereum wrapper through a URI that points to ENS
    uri = Uri('wrap://ens/mainnet/ethereum.polywrap.io')

    # Specify the function to call and its arguments
    options = InvokerOptions(uri=uri, method="balanceOf", args=["0x1234567890123456789012345678901234567890"])

    # Invoke the function and get the result
    result = await client.invoke(options)

    # Print the result
    print(result.result)

# Call the function
await call_ethereum_wrapper()
```

In this example, we are calling the `balanceOf` function of the Ethereum wrapper deployed on the mainnet. We pass in the address `0x1234567890123456789012345678901234567890` as the argument to the function. The `PolywrapClient` is used to invoke the function, and the result is printed to the console. 

