import requests
import os

# Define the dataset of PDF URLs
pdf_urls = {
    "pdf1": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTUwL3ZvbHVtZSAxL1BhcnQgSS9Db21taXNzaW9uZXIgb2YgSW5jb21lIFRheCwgV2VzdCBCZW5nYWxfQ2FsY3V0dGEgQWdlbmN5IEx0ZC5fMTY5NzYwNjMxMC5wZGY=",
    "pdf2": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTUyL3ZvbHVtZSAxL1BhcnQgSS90aGUgc3RhdGUgb2YgYmloYXJfbWFoYXJhamFkaGlyYWphIHNpciBrYW1lc2h3YXIgc2luZ2ggb2YgZGFyYmhhbmdhIGFuZCBvdGhlcnNfMTY5ODMxODQ0OC5wZGY=",
    "pdf3": "https://cdnbbsr.s3waas.gov.in/s380537a945c7aaa788ccfcdf1b99b5d8f/uploads/2024/07/20240716890312078.pdf",
    "pdf4": "https://www.mha.gov.in/sites/default/files/250883_english_01042024.pdf",
    "pdf5": "https://rbidocs.rbi.org.in/rdocs/PressRelease/PDFs/PR60974A2ED1DFDB84EC0B3AABFB8419E1431.PDF",
    "pdf6": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTYwL3ZvbHVtZSAxL1BhcnQgSS90aGUgdGF0YSBvaWwgbWlsbHMgY28uIGx0ZC5faXRzIHdvcmttZW4gYW5kIG90aGVyc18xNjk5MzMzODYyLnBkZg==",
    "pdf7": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTYwL3ZvbHVtZSAxL1BhcnQgSS9ncmVhdCBpbmRpYW4gbW90b3Igd29ya3MgbHRkLiwgYW5kIGFub3RoZXJfdGhlaXIgZW1wbG95ZWVzIGFuZCBvdGhlcnNfMTY5OTMzNjM1NS5wZGY=",
    "pdf8": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTYwL3ZvbHVtZSAxL1BhcnQgSS9tZXNzcnMuIGlzcGFoYW5pIGx0ZC4gY2FsY3V0dGFfaXNwYWhhbmkgZW1wbG95ZWVzICB1bmlvbl8xNjk5MzM4NTQ5LnBkZg==",
    "pdf9": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTYwL3ZvbHVtZSAxL1BhcnQgSS9waHVsYmFyaSB0ZWEgZXN0YXRlX2l0cyB3b3JrbWVuXzE2OTkzMzkyMjYucGRm",
    "pdf10": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTYwL3ZvbHVtZSAxL1BhcnQgSS90aGUgbG9yZCBrcmlzaG5hIHN1Z2FyIG1pbGxzIGx0ZC4sIGFuZCBhbm90aGVyX3RoZSB1bmlvbiBvZiBpbmRpYSBhbmQgYW5vdGhlcl8xNjk5MzQxMDE0LnBkZg==",
    "pdf11": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTYwL3ZvbHVtZSAxL1BhcnQgSS8xNjk5NTIxMzUwLnBkZg==",
    "pdf12": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTYwL3ZvbHVtZSAxL1BhcnQgSS9yaG5jYXJpbWVzc3JvcyBmb3IgY29tY2hlY2sgb2Ygbm93IHJlbW90ZSBsaWZlIHBvcyBhbmQgb2Ygbm93IHJpbmdpb25hbCAxNjk5NTQ4NTM0LnBkZg==",
    "pdf13": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTYwL3ZvbHVtZSAxL1BhcnQgSS90aGUgY29tbWlzc2lvbmVyIG9mIGluY29tZS10YXgsIGJvbWJheV9yYW5jaGhvZGRhcyBrYXJzb25kYXMsIGJvbWJheV8xNjk5NTI2MjI3LnBkZg==",
    "pdf14": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTYwL3ZvbHVtZSAxL1BhcnQgSS8xNjk5NTI2ODA0LnBkZg==",
    "pdf15": "https://digiscr.sci.gov.in/pdf_viewer?dir=YWRtaW4vanVkZ2VtZW50X2ZpbGUvanVkZ2VtZW50X3BkZi8xOTYwL3ZvbHVtZSAxL1BhcnQgSS9zaHJpIGIuIHAuIGhpcmEsIHdvcmtzIG1hbmFnZXIsIGNlbnRyYWwgcmFpbHdheSwgcGFyZWwsIGJvbWJheSBldGMuX3NocmkgYy4gbS4gcHJhZGhhbiBldGMuXzE2OTk1MjcyMTcucGRm",
    "pdf16": "https://www.sebi.gov.in/sebi_data/attachdocs/1292585113260.pdf",
    "pdf17": "https://ijtr.nic.in/Circular%20Orders%20(Supplement).pdf",
    "pdf18": "https://enforcementdirectorate.gov.in/sites/default/files/Act%26rules/The%20Prevention%20of%20Money-laundering%20%28Maintenance%20of%20Records%29%20Rules%2C%202005.pdf"
}



# Create a directory to save the PDFs
output_dir = 'downloaded_pdfs'
os.makedirs(output_dir, exist_ok=True)

# Download each PDF
for name, url in pdf_urls.items():
    try:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()  # Check if the request was successful

        # Define the file path for saving the PDF
        pdf_path = os.path.join(output_dir, f"{name}.pdf")

        # Write the content to a PDF file
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(response.content)

        print(f"Downloaded: {name}.pdf")

    except requests.HTTPError as e:
        print(f"Failed to download {name}: {e}")

    except Exception as e:
        print(f"An error occurred for {name}: {e}")

print("All downloads complete.")
