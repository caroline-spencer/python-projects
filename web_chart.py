from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import json
import ssl
import gviz_api

# This program creates a column chart of United States GDP from the years 1960 to 2021

# This (big) string variable, delimited by triple quotes, contains the template for the HTML and JavaScript to render the chart.
# For more info, see https://developers.google.com/chart/interactive/docs/dev/gviz_api_lib
# Do NOT change this, except for chart customizations that can be specified under options.
column_chart_template = """
<html>
  <head>
    <script src="https://www.google.com/jsapi"></script>
    <script>
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = new google.visualization.DataTable(%(json_text)s);

        var options = {
          title: 'United States GDP 1960 to 2021',
          colors: ['mediumturquoise']
        };

        var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 900px; height: 500px;"></div>
  </body>
</html>
"""


def main():
    # This function returns a dictionary of the year and GDP
    gdp_dictionary = parse_feed()

    # Create the schema, defining the columns and their types
    description = [("Year", "string"), ("GDP", "number")]

    # Create the data
    data = []   # Initialize the list
    # Loop through the dictionary and append a tuple containing the year and GDP to the list
    for year in gdp_dictionary:
        data.append((year, gdp_dictionary[year]))

    # Create a DataTable object
    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    # Convert to JSON -- this text will be substituted into the column_chart_template
    json_text = data_table.ToJSon()
    # print(json_text)

    # Create the html file with Google column chart
    filename = 'US_GDP_web_chart.html'
    try:
        # Create HTML file
        html_file = open(filename, 'w', encoding='utf8')

        # Write the column chart template to the file, substituting in the JSON text
        html_file.write(column_chart_template % vars())

        # Close the file
        html_file.close()
    except ValueError as err:
        print(err)
    except FileNotFoundError as err:
        print(err)
    except OSError as err:
        print(err)
    except Exception as err:
        print(err)


def parse_feed():
    gdp_dictionary = {}
    try:
        # Include the following to avoid this error,  SSL: CERTIFICATE_VERIFY_FAILED
        ssl._create_default_https_context = ssl._create_unverified_context

        feed_url = "http://api.worldbank.org/v2/countries/USA/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json"
        response = urlopen(feed_url)  # open the URL and save HTTP response object
        feed_content = response.read()  # read the data from the response and save

        # Parse the json data to create the GDP dictionary
        feed_dictionary = json.loads(feed_content)
        results = feed_dictionary[1]
        for result in results:
            year = result['date']
            gdp = result['value']
            gdp_dictionary[year] = gdp
        print(gdp_dictionary)
        return gdp_dictionary
    except ValueError as err:
        print('An error occurred trying to decode the json text')
        print(err)
    except HTTPError as err:
        print('Server could not fulfill the request.')
        print(err)
    except URLError as err:
        print('Failed to reach a server.')
        print(err)
    except Exception as err:
        print('An error occurred: ', err)


main()
