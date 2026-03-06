tools = [
    {
        "type": "function",
        "function": {
            "name": "latest_price",
            "description": "Return the most recent Toyota closing stock price",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "average_price_year",
            "description": "Calculate average Toyota closing price for a given year",
            "parameters": {
                "type": "object",
                "properties": {
                    "year": {"type": "integer", "description": "Year to analyze"}
                },
                "required": ["year"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "highest_price",
            "description": "Return highest Toyota closing price in dataset",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "price_on_date",
            "description": "Return Toyota closing price for a specific date",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {"type": "string", "description": "Date format YYYY-MM-DD"}
                },
                "required": ["date"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "average_volume",
            "description": "Return average Toyota trading volume",
            "parameters": {"type": "object", "properties": {}},
        },
    },
]
