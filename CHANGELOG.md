
### Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Carried Forward to Future Exercises

1. Create a separate library for server side python so that Django code only includes Django specific logic. All other logic is in separate libraries which in theory can be used for any other framework (e.g. Flask)
1. Create a class to load the CSV file.
1. Carry out the load and database save in chunks. This will support REST Based paginated GET interfaces to allow load of data in sequence. Such REST interfaces are very common.

## [0.1.0] - 2022-01-22

### Added

1. Create a django project for the Global Monitoring Laboratory of the NOAA `django-admin startproject gml`
1. Rename the top level directory to backend `mv gml backend`. This doesn't effect the django app. The project inside is still gml.
1. Create an application for Carbon Cycle Greenhouse Gases `python manage startapp ccgg`
1. Download Mauna Loa CO_2 monthly mean data from `https://gml.noaa.gov/ccgg/trends/data.html`
1. Create a model for the data CO2_MM_MLO, generate and run migrations.
1. Create management app `ccgg/management/commands/load_csv` to load the data into the database.
1. Create management app `ccgg/management/commands/generate_graph` to generate average and interpolated as per problem 7.1.4 of Hill. Graphs are generated into application static directory. These are not under version control.
1. Created route to home page `ccgg/` which is rendered by `views.index` using `ccgg/index.html` template.

