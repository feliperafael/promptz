import yaml

from promptsy.prompt_manager import PromptManager

class Prompt:
    """
    A class representing a prompt.

    Args:
        name (str): The name of the prompt.
        description (str): A brief description of the prompt.
        template (str): The template string for the prompt.
    """

    def __init__(self, name, description, template):
        """
        Initialize a new Prompt instance.

        Args:
            name (str): The name of the prompt.
            description (str): A brief description of the prompt.
            template (str): The template string for the prompt.
        """
        self.name = name
        self.description = description
        self.template = template
        self.prompt_manager = PromptManager()

    def format(self, **kwargs):
        """
        Format the prompt template with the provided keyword arguments.

        Args:
            **kwargs: Keyword arguments to be used for formatting the template.

        Returns:
            str: The formatted prompt string.
        """
        return self.template.format(**kwargs)

    def __str__(self):
        """
        Return a string representation of the Prompt instance.

        Returns:
            str: The string representation of the Prompt instance.
        """
        return f"{self.name}: {self.description}"

    def to_dict(self):
        """
        Convert the Prompt instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Prompt instance.
        """
        return {
            'name': self.name,
            'description': self.description,
            'template': self.template
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Prompt instance from a dictionary.

        Args:
            data (dict): A dictionary containing the prompt data.

        Returns:
            Prompt: A new Prompt instance created from the dictionary.
        """
        # Ensure data is a dictionary
        if not isinstance(data, dict):
            raise ValueError("Expected a dictionary for data")
        return cls(data['name'], data['description'], data['template'])

    def save(self):
        """
        Save the Prompt instance using the provided PromptManager.

        Args:
            manager (PromptManager): The PromptManager instance to use for saving the prompt.
        """
        self.prompt_manager.save(self.to_dict(), self.name)

    @classmethod
    def load(cls, name):
        """
        Load a Prompt instance using the provided PromptManager and prompt name.

        Args:
            manager (PromptManager): The PromptManager instance to use for loading the prompt.
            name (str): The name of the prompt to load.

        Returns:
            Prompt: The loaded Prompt instance.
        """
        from promptsy.prompt_manager import PromptManager
        prompt_manager = PromptManager()
        data = prompt_manager.load(name)  # Check what this returns
       
        return data
    
    def get_description(self):

        print(self.description)
