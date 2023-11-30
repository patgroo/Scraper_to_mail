import datetime
import os


def create_html_from_scraper(scraped_list):

    html = """\
    <html>
    <body>
        <table>
        <tbody>
            {}
        </tbody>
        </table>
    </body>
    </html>
    """

    rows = ""
    for article in scraped_list:
        rows += "<tr><td>" + str(article) + "</td></tr>"

    html = html.format(rows)

    # Generate filename based on current date and time
    filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".html"

    # Check if the 'html' directory exists and create it if not
    if not os.path.exists("html"):
        os.makedirs("html")

    # Save the HTML content to a file
    with open(os.path.join("html", filename), 'w') as file:
        file.write(html)

    return html
