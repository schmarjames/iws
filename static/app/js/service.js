const api =  "https://iws-api-heroku.herokuapp.com/api/v1.0/";
const Service = {
  getAllFeature: () => $.ajax({
    url: `${api}features`,
    method: "GET"
  }),
  addFeature: (data) => $.ajax({
    url: `${api}features`,
    method: "POST",
    data: data
  })
}

export default Service;
