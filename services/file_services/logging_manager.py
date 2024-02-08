from datetime import datetime as dt


class LoggingManager:
    def __init__(self) -> None:
        pass

    def save_message(self, message: str):
        with open(f'files/logs/{dt.now().strftime("%Y-%m-%d-%H")}-app.log', 'a') as file_writer:
            file_writer.write(message)
