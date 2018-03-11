class Feature {
  constructor(opt) {
    this.title = null;
    this.description = null;
    this.client_id = null;
    this.priority_id = null;
    this.target_data = null;
    this.product_area_id = null;

    this.merge_parameters(opt);
  }

  merge_parameters(opts) {
    for (var i in opts) {
      if (this.hasOwnProperty(i)) {
        this[i] = opts[i];
      }
    }
  }

  speak() {
    return 'this is the feature obj';
  }
}

export default Feature;
