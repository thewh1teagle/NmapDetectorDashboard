var dashboard = $(".dashboard")
var dashboard_ul = $(".list-group")
// var ul_container = $(".ul-container")
var ul_container = $(".ul-container")

const add_li_element = function(IP, TIMESTAMP, PORTS) {
  dashboard_ul.append(
    `
    <li class="list-group-item" style="padding-left: 50px; padding-right: 50px;">
           <h5  style="display: inline; border-left: 1px solid red; border-right: 1px solid red; margin-left: 10px; margin-right: 10px;">IP ${IP}</h2>
           <h5 style="display: inline; border-left: 1px solid red; border-right: 1px solid red;">TIMESTAMP ${TIMESTAMP}</h2>
           <h5 style="display: inline; border-left: 1px solid red; border-right: 1px solid red;">PORTS ${PORTS}</h2>
    </li>
    `
  )
}

console.log("hi")

// dashboard_ul.scroll(function() {
//   console.log("scroll")
// })


ul_container.on('scroll', function() {
  
  var ul_container_height = ul_container.height()
  var current_position = ul_container.scrollTop()
  // if (current_position >= ul_container_height / 100 * 75) {
  //   console.log("loading..")
  // }
  console.log(current_position)
  console.log(ul_container_height)
})


