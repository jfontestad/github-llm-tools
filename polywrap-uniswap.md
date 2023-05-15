-> **Question**: Create a sample call to the uniswap wrapper using the polywrap python client. 

**Answer**: Here's an example of how to call the Uniswap wrapper using the Polywrap Python client:

```python
from polywrap_client import PolywrapClient
from polywrap_core import Uri, InvokerOptions

async def swap_tokens(client: PolywrapClient, from_token: str, to_token: str, amount_in: int):
    
    # Instantiate the client
    client = PolywrapClient()
    
    # Load the Uniswap WebAssembly wrapper through a URI that points to the Polywrap Registry
    uri = Uri('wrap://ens/ropsten/uniswap-v3.polywrap.eth')

    # Set the arguments for the swapTokens function
    args = {
        'fromToken': from_token,
        'toToken': to_token,
        'amountIn': amount_in,
        'slippage': 0.01,
        'recipient': '0x1234567890123456789012345678901234567890',
        'deadline': 1718425031,
        'swapType': 'EXACT_INPUT',
    }

    # Configure the client
    options = InvokerOptions(
        uri=uri, method="swapTokens", args=args, encode_result=False
    )
    
    # Invoke the wrapper 
    result = await client.invoke(options)

    return result.result
``` 

Note that you'll need to replace the `from_token`, `to_token`, `amount_in`, `recipient`, `deadline`, and `swapType` values with your own values in order to make a successful call to the Uniswap wrapper. Also make sure to import the PolywrapClient and Uri from the right package. 

