/**
 * Updates the current color, distance and motor status calling
 * the corresponding methods.
 */
function updateStatus() {
    // Update current color based on Open CV

    (async () => await updateCurrentColorOpenCV())();
    // Update motor status
    //...
    updateMotorStatus(status);
    // Update current color based on OpenCV
    //...

    // Update current distance
    //...
    updateDistance();

    updateCurrentColorDistance();
}

/**
 * Update the current color based on OpenCV.
 */
async function updateCurrentColorOpenCV() {
    try {
        // Request color from server
        const requestResult = await requestColorFromOpenCV()
        // Get the HTML element where the status is displayed
        const blue_open_cv = document.getElementById('blue_open_cv')
        blue_open_cv.innerHTML = requestResult.data[0]
        const purple_open_cv = document.getElementById('purple_open_cv')
        purple_open_cv.innerHTML = requestResult.data[1]
        const yellow_open_cv = document.getElementById('yellow_open_cv')
        yellow_open_cv.innerHTML = requestResult.data[2]
        const green_open_cv = document.getElementById('green_open_cv')
        green_open_cv.innerHTML = requestResult.data[3]

    } catch (e) {
        console.log('Error getting the color based on OpenCV', e)
        updateStatus('Error getting the color based on OpenCV')
    }
}

/**
 * Function to request the server to update the current
 * color based on OpenCV.
 */
function requestColorFromOpenCV() {
    try {
        // Make request to server
        return axios.get('/get_color_from_opencv')
    } catch (e) {
        console.log('Error getting the status', e)
        updateStatus('Error getting the status')

    }
}


/**
 * Function to request the server to start the motor.
 */
function requestStartMotor() {
    try {
      return axios.get('/start_motor')
    } catch (e) {
      console.log('Error getting the start request', e)
      updateStatus('Error getting the start request')
    }
  }


/**
 * Function to request the server to stop the motor.
 */
function requestStopMotor () {
    try {
      return axios.get('/stop_motor')
    } catch (e) {
      console.log('Error getting the stop request', e)
      updateStatus('Error getting the stop request')
    }
}

/**
 * Update the status of the motor.
 * @param {String} status
 */
function updateMotorStatus(status) {
    // Get the HTML element where the status is displayed
    axios.get('/motor_status')
  .then((response) => {
    const motor_status_html_element = document.getElementById('motor')
    if (response.data.success){motor_status_html_element.innerHTML = "Motor is working"}
    else{motor_status_html_element.innerHTML = "Motor is not working"}

  })
}

/**
 * Update the current color based on distance sensor.
 */
function updateDistance() {
    // Get the HTML element where the status is displayed
    // ...
    try {
    const requestResult = requestDistance()
  } catch (e) {
    console.log('Error getting the distance', e)
    updateStatus('Error getting the distance')
  }
}


/**
 * Function to request the server to get the distance from
 * the rod to the ultrasonic sensor.
 */
async function requestDistance() {
    //...
    try {
    // Make request to server
    let result = await axios.get('/get_distance')
    let distance = document.getElementById("distance")
    distance.innerText = result.data.distance
  } catch (e) {
    console.log('Error getting the distance request', e)
    updateStatus('Error getting the distance request')
  }
}


/**
 * Update the current color based on distance sensor.
 */
function updateCurrentColorDistance() {
    // Get the HTML element where the status is displayed
    try {
    const requestResult = requestColorFromDistance()
  } catch (e) {
    console.log('Error getting the current color from distance', e)
    updateStatus('Error getting the current color from distance')
  }
}


/**
 * Function to request the server to get the color based
 * on distance only.
 */
async function requestColorFromDistance() {
    try {
    let result = await axios.get('/get_color_from_distance')
    let blue_color = document.getElementById("blue_color")
    blue_color.innerText = result.data.blue_color[0]
    let purple_color = document.getElementById("purple_color")
    purple_color.innerText = result.data.purple_color[1]
    let yellow_color = document.getElementById("yellow_color")
    yellow_color.innerText = result.data.yellow_color[2]
    let green_color = document.getElementById("green_color")
    green_color.innerText = result.data.green_color[3]
  } catch (e) {
    console.log('Error getting the current color from distance', e)
    updateStatus('Error getting the current color from distance')
  }
}
