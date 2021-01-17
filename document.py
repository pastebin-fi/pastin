from flask import abort, render_template, request
import json
import os.path

class Document:

    def __init__(self, app, document_manager, data: dict):
        self.app = app
        self.document_manager = document_manager

        self.name = data["name"]
        self.url = data["url"]
        self.id = data["id"]
        self.file_path = data["file"]
        self.visible = data["visible"]

    def register_endpoint(self):
        self.app.add_url_rule(self.url, self.id, self.document_manager.endpoint)

    def get_md(self):
        # TODO: Cache documents
        with open(self.file_path, "r", encoding="utf-8") as f:
            data = f.read()
        return data


class DocumentManager:

    def __init__(self, app, config_path: str):
        self.app = app

        self.config_path = config_path
        with open(config_path, "r", encoding="utf-8") as f:
            data = f.read()

        data = json.loads(data)
        # The key in self.documents is the document's ID
        self.documents = {}
        for document_data in data:
            document = Document(app, self, document_data)
            self.documents[document.id] = document

        for document_id, document in self.documents.items():
            document.register_endpoint()

    def endpoint(self):
        if request.endpoint not in self.documents:
            abort(404)
        else:
            document = self.documents[request.endpoint]
            return render_template("document.html", data=document.get_md())
