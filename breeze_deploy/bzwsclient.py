import websocket


class TickHandler:
    def __init__(self):
        pass

    def on_ticks(self, ticks):
        # Your logic to handle incoming ticks
        print("Received ticks:", ticks)


class WebSocketClient:
    def __init__(self, url):
        self.url = url
        self.ws = None

    def on_message(self, message):
        # Your logic to handle incoming messages
        print("Received message:", message)

    def on_error(self, error):
        # Your error handling logic
        print("Error:", error)

    def on_close(self):
        # Your logic for handling the WebSocket close event
        print("WebSocket closed.")

    def connect(self):
        # Create a WebSocket connection and set event handlers
        self.ws = websocket.WebSocket(self.url,
                                        on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.run_forever()

    def get_on_ticks_function(self):
        # Return the on_ticks function from the TickHandler class
        tick_handler = TickHandler()
        return tick_handler.on_ticks


# Example usage:
if __name__ == "__main__":
    url = "ws://example.com/websocket"  # Replace with your WebSocket URL
    ws_client = WebSocketClient(url)
    ws_client.connect()
    # Get the on_ticks function from the TickHandler class
    on_ticks_function = ws_client.get_on_ticks_function()

    # Now you can use `on_ticks_function` as a standalone function to handle incoming ticks.
    # You can also pass it to other functions or WebSocket/event listeners as needed.
