"""contains functions for converting dictionary to an html or pdf file"""
import webbrowser
from fpdf import FPDF


def convert_to_html(news: dict, path: str):
    with open(path, "w", encoding="utf-8") as html_file:
        for item in news:
            html_item = f''' 
                        <a href="{item["link"]}" class="list-group-item list-group-item-action d-flex gap-3 py-3" \\ 
                        aria-current="true">
                            <img src="{item["image"]}" alt="" width="150" class= flex-shrink-0">
                            <div class="d-flex gap-2 w-100 justify-content-between">
                            <div>
                                <p class="h5">{item["title"]}</p>
                                <p class="mb-0 opacity-75">{item["description"]}</p>

                            </div>
                            <small class="opacity-50 text-nowrap">{item["pubDate"]}</small>
                            </div>
                        </a>
                        '''

            html_file.write(html_item)
        footer = '''
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"\\
                         integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" \\
                             crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" \\
                ttf2pt1 -a font.ttf font        integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p"\\
                             crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" \\ 
                    integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF"\\
                         crossorigin="anonymous"></script>
                    </body>
                    </html>
                    '''

        html_file.write(footer)
        print("Html file created successfully!!")
        webbrowser.open_new_tab(path)


class PDF(FPDF):
    """Class for creating a pdf file and adding news to it"""

    def __init__(self, news, path):
        super().__init__()
        self.news = news
        self.path = path

    def create_pdf(self):
        """adds a page to the pdf file with font and news"""
        self.add_page()
        self.add_font('DejaVu', '', 'project/Font/DejaVuSansCondensed.ttf', uni=True)

        self.set_auto_page_break(auto=True, margin=15)
        for item in self.news:
            self.set_font('DejaVu', '', 15)
            self.multi_cell(0, 10, f"{item['title']}", border=True, align="C")
            self.set_font('DejaVu', '', 13)
            self.multi_cell(0, 5, f"{item['description']}")
            self.ln()
            self.cell(0, 5, f"PubDate: {item['pubDate']}")
            self.ln()
            self.cell(0, 5, "Link (Clickable)", link=item['link'], ln=True)
            self.cell(0, 10, "Image (Clickable)", link=item['image'], ln=True)
            self.ln()
        self.output(self.path)
        print("\nSuccessful write to pdf!\n")
        return True
