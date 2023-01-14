task = []
time = []

const mainDiv = document.querySelector('#mainDiv')


button.onclick = function() {
  var output = document.createElement('li');
  output.innerHTML = document.getElementById('task').value + '  --  ' + document.getElementById('time').value;
  task.push(document.getElementById('task').value)
  time.push(document.getElementById('time').value)
  mainDiv.appendChild(output);
};

mainDiv.appendChild(button);

