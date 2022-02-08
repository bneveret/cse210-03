#this file handles terminal operations
import random
class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output(text or numerical) operations for the 
    terminal.
    """    
     
    def read(self, prompt):
        """Gets text input from the user through the screen.
        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.
        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_letter(self, prompt):
        """Gets numerical input from the user through the screen.
        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.
        Returns:
            float: The user's input as a float.
        """
        return float(input(prompt))
        
    def write(self, text):
        """Displays the given text on the screen. 
        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)