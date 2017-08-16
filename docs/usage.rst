=====
Usage
=====

To use HTML dumper in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'html_dumper.apps.HtmlDumperConfig',
        ...
    )


This app adds a django command !

```
python manage.py dump_html [path/to/my/page1 my/page2] (default to ['/', ])
```

You can use either relative or absolute URLs. Note that you might need to add 'testserver' in your `settings.ALLOWED_HOSTS`.

This will create a directory `HTML_OUTPUT` (name can be customized via `settings.SITE_OUTPUT_DIRECTORY`) which will contain :
- the content of the page under the given urls for all available languages
- the static folder (copied from the output of `collectstatic`, beware of all the admin assets...)

You can have a look at the `example` folder to give it a try.

