var current = null;
document.querySelector('#email').addEventListener('focus', function (e) {
  if (current) current.pause();
  current = anime({
    targets: 'path',
    strokeDashoffset: {
      value: 0,
      duration: 700,
      easing: 'easeOutQuart'
    },
    strokeDasharray: {
      value: '240 1386',
      duration: 700,
      easing: 'easeOutQuart'
    }
  });
});
document.querySelector('#password').addEventListener('focus', function (e) {
  if (current) current.pause();
  current = anime({
    targets: 'path',
    strokeDashoffset: {
      value: -336,
      duration: 700,
      easing: 'easeOutQuart'
    },
    strokeDasharray: {
      value: '240 1386',
      duration: 700,
      easing: 'easeOutQuart'
    }
  });
});
document.querySelector('#submit').addEventListener('focus', function (e) {
  if (current) current.pause();
  current = anime({
    targets: 'path',
    strokeDashoffset: {
      value: -730,
      duration: 700,
      easing: 'easeOutQuart'
    },
    strokeDasharray: {
      value: '530 1386',
      duration: 700,
      easing: 'easeOutQuart'
    }
  });
});

// redirection after the post request
function redirect() {
  window.location.replace("./about");
}

if (document.getElementById("login-form")) {
  document.getElementById("login-form").addEventListener("submit", function (e) {
    e.preventDefault();
    var form = document.getElementById("login-form");
    var data = new FormData(form);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/login", true);
    xhr.onload = function () {
      if (this.status == 200) {
        redirect();
      }
    };
    xhr.send(data);
  });
}