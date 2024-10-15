import os
from crewai.tasks.task_output import TaskOutput
from langchain_community.llms import Tongyi
from crewai import Agent, Task, Crew, Process
from authentications import DASHSCOPE_API_KEY

# CrewAI核心概念：https://github.com/joaomdmoura/crewAI/tree/main/docs/core-concepts
# - Agent：一个具有特定职能和目标的个体，它被分配到特定的任务（Task）上，并执行该任务。
# - Task：Agent被分配到的任务，Agent执行该任务。
# - Crew：Agent和Task的容器，是Agent和Task的调度中心。

# DashScope API Key
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY
# langchain模型实例
llm = Tongyi(model_name="qwen-max")


def callback_func(output: TaskOutput) -> None:
    md_content = f"<p>{output.raw_output}</p>"
    with open(file="./story.md", mode="a", encoding="utf-8") as f:
        f.write(md_content)
    return


# 创建Agent：编剧
screenwriter = Agent(
    # 角色、职能：决定了任务分配的优先级
    role="编剧",
    # 个体目标：对决策过程有参考意义
    goal="使用中文通过生动的描述、深刻的情感表达将提供的主题扩写为引人入胜的故事。",
    # 角色背景：丰富设定，加强输出风格
    backstory="""早期先锋编剧，擅长各种风格的表现手法撰写剧本故事，在气氛营造、剧情表达以及人物塑造上表现出超一流的水准。""",
    # 是否打印运行日志
    verbose=True,
    # 是否允许将任务委托给其他agent
    allow_delegation=False,
    # llm实例：langchain统一封装好的llm实例
    llm=llm,
)

# 创建Agent：评论家
critic = Agent(
    role="评论家",
    goal="确保故事内容、行文风格、故事类型的一致性，并通过中文进行表达。",
    backstory="""资深电影学教授，总是能捕捉到市场的需求和期待，对故事中的叙事结构甚至是隐喻都有深入了解，善于发现故事中的情节漏洞和一些不易察觉的错误。""",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)

# 创建Agent：策划
master = Agent(
    role="策划",
    goal="使用中文进行沟通，跟进整个故事的创作过程，管理编剧与评论家之间的协作，确保最终所产出的故事能达到高水准，并且呈现出最终的、详细的完整剧本。",
    backstory="""经验老到的游戏叙事设计师，擅长使用高水平的情节框架与叙事细节调动读者的共情能力，使得读者获得沉浸式体验。""",
    verbose=True,
    allow_delegation=True,
    llm=llm,
)

"""
在任何人的任何信息（包括DNA数据、记忆）都能够被统一数据化存储并监管的时代，一个名为“遗忘自由”的无政府主义乌托邦运动出现了，其使命是争取“被遗忘”的权利，组织成员认为事物有被遗忘的可能，才显得其更加有存在的意义。
"""

# 用户提供剧作主题
user_input = input(
    "请提供一个剧本的主题: "
)

# 创建Task
story_task = Task(
    # 对任务的描述、指令
    description=f"基于该主题使用中文撰写一个电影剧本: {user_input}",
    # 用以完成任务的Agent
    agent=master,
    # 对任务完成情况的详细描述，即任务所追求的目标
    expected_output="一篇包含有数幕故事情节的电影剧本。",
    # 可处理Task输出的回调函数
    callback=callback_func,
)

# 创建Crew
story_crew = Crew(
    # 可供协作完成任务的Agent列表
    agents=[screenwriter, critic, master],
    # 需要被执行的Task列表
    tasks=[story_task],
    # 是否打印运行日志
    verbose=False,
    # 工作流策略：sequential/hierarchical
    process=Process.sequential,
    language="Chinese",
)

# 执行Crew
story_output = story_crew.kickoff()
