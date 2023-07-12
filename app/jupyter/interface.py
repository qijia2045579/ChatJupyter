import ipywidgets as widgets
from tqdm.notebook import tqdm, trange
import time
from IPython.display import display, HTML
from IPython.display import clear_output
import pathlib
import logging
import warnings
import requests


class jupyter_interface:
    """
    The main class build for ipython kernel to interact with the castle serveless content
    if a widget's value will be changed or acquired later, it will become to class member,
    otherwise, they keep in temporary
    """
    
    def __init__(self):
        # Progressing the Initiation steps
        self.init_loading()

    def init_loading(self):
        # init the window
        self.init_window()
        
    def init_window(self):
        self.init_style()
        self.title_bar = self.init_title_bar()
        self.question_button = self.init_question()
        self.data_search_button = self.init_data_search()
        self.summary_button = self.init_summary()
        
        tasks_h = widgets.HBox([self.question_button, self.data_search_button, self.summary_button])
        
        # self.conversation = self.init_conversation()
        
        
        self.window = widgets.VBox([self.title_bar, tasks_h])
        
        # self.out = widgets.outputs
        
    def init_data_search(self):
        new_data_search = widgets.Button(
                                        description='Document Based QA',
                                        disabled=False,
                                        button_style='info',
                                        tooltip='Click to get business name reference',
                                        layout={'width': 'max-content'}
                                    )
        new_data_search.on_click(self.create_DS_block)
        return new_data_search
        
    def init_summary(self):
        new_summary = widgets.Button(
                                        description='Text Summarization',
                                        disabled=False,
                                        button_style='info',
                                        tooltip='Click to get summarization',
                                        layout={'width': 'max-content'}
                                    )
        new_summary.on_click(self.create_summary_block)
        return new_summary
    
    def create_summary_block(self, b):
        Guide = widgets.HTML()
        Guide.value = self.stylize_html(f'Summary the given text in few sentence')
        Question = widgets.Textarea(
                                value='',
                                placeholder='Text Here:',
                                disabled=False,
                                layout={'width': '70%'}
                            )
        Think = widgets.Button(
                                description='Summarize it',
                                disabled=False,
                                button_style='success',
                                tooltip='Click to run LLM to summarize',
                                layout={'width': 'max-content'}
                            )
        Answer = widgets.HTML()
        Answer.value = self.stylize_html(f'LLM response here~')
        Divider = widgets.HTML()
        Divider.value = self.stylize_html(f'{"-"*50}')
        
        def think_question(c):
            question = Question.value
            Answer.value = self.stylize_html('I am thinking...')
            # r = requests.post(url='http://10.128.0.171:9888/post_question', data={'question':str(question)})
            r = requests.post(url='http://10.128.0.27:9888/post_openai_conv_sum', data={'question':str(question)})
            # extracting response text
            result = r.text
            Answer.value = self.stylize_html(result)
        
        Think.on_click(think_question)
        
        one_conversation = widgets.VBox([Guide, Question, Think, Answer, Divider])
        
        self.window.children=tuple(list(self.window.children) + [one_conversation]) 
        
        
        
        
        
    def init_question(self):
        new_question = widgets.Button(
                                        description='Common Question',
                                        disabled=False,
                                        button_style='info',
                                        tooltip='Click to have a new conversation',
                                        layout={'width': 'max-content'}
                                    )
        new_question.on_click(self.create_QA_block)
        return new_question
    
    # def init_conversation(self):
    #     self.new_question_button = 
        
    
    def create_DS_block(self, b):
        Guide = widgets.HTML()
        Guide.value = self.stylize_html(f'Search Data Warehouse column name information')
        Question = widgets.Text(
                                value='',
                                placeholder='Ask questions:',
                                disabled=False,
                                layout={'width': '40%'}
                            )
        Think = widgets.Button(
                                description='Answer it',
                                disabled=False,
                                button_style='success',
                                tooltip='Click to run LLM to answer',
                                layout={'width': 'max-content'}
                            )
        Answer = widgets.HTML()
        Answer.value = self.stylize_html(f'LLM response here~')
        Divider = widgets.HTML()
        Divider.value = self.stylize_html(f'{"-"*50}')
        
        def think_question(c):
            question = Question.value
            Answer.value = self.stylize_html('I am thinking...')
            # r = requests.post(url='http://10.128.0.171:9888/post_question', data={'question':str(question)})
            r = requests.post(url='http://10.128.0.27:9888/post_openai_doc_question', data={'question':str(question)})
            # extracting response text
            result = r.text
            Answer.value = self.stylize_html(result)
        
        Think.on_click(think_question)
        
        
        
        one_conversation = widgets.VBox([Guide, Question, Think, Answer, Divider])
        
        self.window.children=tuple(list(self.window.children) + [one_conversation]) 
    
    
    
    
    def create_QA_block(self, b):
        Guide = widgets.HTML()
        Guide.value = self.stylize_html(f'Ask Some Question to the LLM')
        Question = widgets.Text(
                                value='',
                                placeholder='Type something',
                                disabled=False,
                                layout={'width': '40%'}
                            )
        Think = widgets.Button(
                                description='Answer it',
                                disabled=False,
                                button_style='success',
                                tooltip='Click to run LLM to answer',
                                layout={'width': 'max-content'}
                            )
        Answer = widgets.HTML()
        Answer.value = self.stylize_html(f'LLM response here~')
        Divider = widgets.HTML()
        Divider.value = self.stylize_html(f'{"-"*50}')
 
        
        def think_question(c):
            question = Question.value
            Answer.value = self.stylize_html('I am thinking...')
            # r = requests.post(url='http://10.128.0.171:9888/post_question', data={'question':str(question)})
            r = requests.post(url='http://10.128.0.27:9888/post_openai_question', data={'question':str(question)})
            # extracting response text
            result = r.text
            Answer.value = self.stylize_html(result)
        
        Think.on_click(think_question)
        
        
        
        one_conversation = widgets.VBox([Guide, Question, Think, Answer, Divider])
        
        self.window.children=tuple(list(self.window.children) + [one_conversation]) 
        
    
    # init title bar
    def init_title_bar(self):
        space = "&emsp;"
        # title_text = f"{space*9}CASTLE HUB{space*9}"
        title_text = "ChatA&BC -- VoiceAI LLM"
        title = widgets.HTML()
        # https://tholman.com/github-corners/
        title_corner_html = """
<a href="https://github.aetna.com/voice-ai/voice_ai_llm" target="_blank" class="github-corner" aria-label="View source on GitHub"><svg width="80" height="80" viewBox="0 0 250 250" style="fill:#70B7FD; color:#fff; position: absolute; top: 0; border: 0; right: 0;" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg></a><style>.github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}@keyframes octocat-wave{0%,100%{transform:rotate(0)}20%,60%{transform:rotate(-25deg)}40%,80%{transform:rotate(10deg)}}@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}</style>
        """
#         title_corner_html = """
# <a href="https://github.aetna.com/voice-ai/voice_ai_llm"><img decoding="async" loading="lazy" width="149" height="149" src="https://github.blog/wp-content/uploads/2008/12/forkme_right_white_ffffff.png?resize=149%2C149" class="attachment-full size-full" alt="Fork me on GitHub" data-recalc-dims="1"></a>
#         """
        title.value = self.stylize_html(f'<h1 class="animate__animated animate__flash" style="color: #80B5F7;">{title_corner_html}{space*5}{title_text}</h1>')
        box_layout = widgets.Layout(display='flex',
                                    flex_flow='column',
                                    align_items='stretch',
                                    width='100%',
                                    height='10')
        title_bar = widgets.HBox([title], layout=box_layout)
        return title_bar
    
        
        
    # Common functions
    def init_style(self):
        # base style from bootstrap
        base_style = """
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        """
        # animated style from animate.css
        animated_style = """
<link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
  />
        """
        
        self.main_style = f"""
<head>
{base_style}
{animated_style}
</head>
        """
    
    def stylize_html(self, content):
        return self.main_style+content
    
    def show(self):
        return self.window