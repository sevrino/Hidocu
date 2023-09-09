"use strict"

let fileInput = document.getElementById("fileUpload");
let filename = document.getElementById("FileName");
let version = document.getElementById("version");

let file = btoa(fileInput);
let date = Date.now();

const submitButton = document.querySelector("#submit");

submitButton.addEventListener("click", submit);

let req = {"filename": filename, "file": fileInput, "version": version, "date":date};

fetch("localhost:8080/upload", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify(req)
})
    .then((res) => res.json())
    .then((res) => {
        if (res['status'] == 'ok') {
            alert("파일 업로드 완료.");
        } else {
            alert(res.msg);
        }
    });

