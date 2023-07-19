import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def generate_html_table(data):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Navigable HTML Table with Filters</title>
        <style>
            /* Add your CSS styling here */
        </style>
    </head>
    <body>
        <h1>Navigable HTML Table with Filters</h1>
        <table id="data-table" border="1">
            <tr>
                <th>STATUS</th>
                <th>PROPERTIES_metadata_displayName</th>
            </tr>
            {% for row in data %}
            <tr>
                <td>{{ row['STATUS'] }}</td>
                <td>{{ row['PROPERTIES_metadata_displayName'] }}</td>
            </tr>
            {% endfor %}
        </table>
        <script>
            // Add your JavaScript code here to implement table filtering
        </script>
    </body>
    </html>
    """

    return html_content.replace('\n    ', '\n')

def main():
    csv_file = 'data.csv'  # Replace with the path to your CSV file
    data = read_csv_file(csv_file)
    html_table = generate_html_table(data)

    with open('output.html', 'w') as html_file:
        html_file.write(html_table)

if __name__ == "__main__":
    main()
