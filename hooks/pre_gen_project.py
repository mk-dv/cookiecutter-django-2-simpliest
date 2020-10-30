import sys

project_slug = "{{ cookiecutter.project_slug }}"
if hasattr(project_slug, "isidentifier"):
    assert (
        project_slug.isidentifier()
    ), f"'{ project_slug }' project slug is not a valid Python identifier."

assert (
    project_slug == project_slug.lower()
), f"'{ project_slug }' project slug should be all lowercase"

assert (
    "\\" not in "{{ cookiecutter.author_name }}"
), "Don't include backslashes in author name."
