task = []
time = []

const mainDiv = document.querySelector('#mainDiv')
const listSection = document.querySelector('#planSection')


button.onclick = function() {
  var output = document.createElement('li');
  output.innerHTML = document.getElementById('task').value + '   --    ' + document.getElementById('time').value + ' minutes';
  task.push(document.getElementById('task').value)
  time.push(document.getElementById('time').value)
  listSection.appendChild(output);
};

mainDiv.appendChild(button);


function planDay() {
    const beginT = timeSet()[0]
    const finishT = timeSet()[1]
    console.log(beginT)

}

function timeSet() {
    const startT = document.querySelector('#startTime').value
    const endT =  document.querySelector('#endTime').value

    x = [startT, endT]

    return x

}






