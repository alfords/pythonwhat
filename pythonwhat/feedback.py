import re
from pythonwhat import utils

# TODO (Vincent): refactor using .format()
class FeedbackMessage(object):
    """Generate feedback.

    Don't use this yet!

    This class will hold all functionality which is related to feedback messaging. 
    At the moment it is NOT used, feedback generation is still HIGLY interwoven with
    test_... files. Should be decoupled. 

    Class should be refactored to use .format() instead.

    Will be documented when it's refactored.
    """
    def __init__(self, message_string):
        self.set(message_string)
        self.information = {}

    def add_information(self, key, value):
        if (not(key in self.information)):
            self.set_information(key, value)

    def set_information(self, key, value):
        self.information[key] = utils.shorten_str(str(value))

    def remove_information(self, key):
        if (key in self.information):
            self.information.pop(key)

    def set(self, message_string):
        self.message_string = str(message_string)

    def append(self, message_string):
        self.message_string += str(message_string)

    def cond_append(self, cond, message_string):
        self.message_string += "${{" + \
            str(cond) + " ? " + str(message_string) + "}}"

    def generateString(self):
        generated_string = FeedbackMessage.replaceRegularTags(
            self.message_string, self.information)
        generated_string = FeedbackMessage.replaceConditionalTags(
            generated_string, self.information)
        return(generated_string)

    def replaceRegularTags(message_string, information):
        generated_string = message_string

        pattern = "\${([a-zA-Z]*?)}"

        keywords = re.findall(pattern, generated_string)
        for keyword in keywords:
            replace = "\${" + keyword + "}"
            if (keyword in information):
                generated_string = re.sub(
                    replace, information[keyword], generated_string)
            else:
                generated_string = re.sub(replace, "", generated_string)

        return(generated_string)

    def replaceConditionalTags(message_string, information):
        generated_string = message_string

        pattern = "\${{([a-zA-Z]*?) \? (.*?)}}"

        cond_keywords = re.findall(pattern, message_string)
        for (keyword, k_string) in cond_keywords:
            replace = "\${{" + keyword + " \? " + re.escape(k_string) + "}}"
            if (keyword in information):
                generated_string = re.sub(
                    replace,
                    " " +
                    FeedbackMessage.replaceRegularTags(
                        k_string,
                        information),
                    generated_string)
            else:
                generated_string = re.sub(replace, "", generated_string)

        return(generated_string)
