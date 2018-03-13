const api =  "https://iws-api-heroku.herokuapp.com/api/v1.0/";
const Service = {
  getAllFeature: () => $.ajax({
    url: `${api}features`,
    method: "GET"
  }),
  addFeature: (data) => $.ajax({
    url: `${api}features`,
    method: "POST",
    data: data,
    contentType: "application/json",
    dataType: "json",
  }),
  getFormFeatureData: (endpoints) => endpoints.map(
    (endpoint) => $.ajax({
        url: `${api}${endpoint}`,
        method: "GET"
    })
  )
}

export default Service;
