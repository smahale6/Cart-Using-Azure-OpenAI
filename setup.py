from setuptools import find_packages,setup

setup(
      name             = 'cart',
      version          = '0.0.0',
      author           = 'Lord Shrikanth',
      author_email     = 'shrikanth.mahale@gmail.com',
      install_requires = [ "transformers","python-dotenv","langchain","langchain_chroma","langchain_community","langchain_openai","openai","PyMuPDF","accelerate","langchain_core","pandas","pyodbc"],
      packages         = find_packages()
)