"use strict"

const loginButton = document.querySelector("#login");

loginButton.addEventListener("click", submit);

const req = {
    username: document.getElementById("#username").value,
    password: document.getElementById("#password").value,
};

fetch("/api/login", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify(req),
})
    .then((res) => res.json())
    .then((res) => {
        if (res.success) {
            alert("로그인 성공");
        } else {
            alert("로그인에 실패하였습니다. ID와 비밀번호를 다시 확인해 주세요.");
        }
    });

