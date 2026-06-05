import {
 BrowserRouter,
 Routes,
 Route
} from "react-router-dom";

import Home from "./components/Home/Home";
import Login from "./components/Login/Login";
import Register from "./components/Register/Register";
import DealerDetails from "./components/DealerDetails/DealerDetails";
import AddReview from "./components/AddReview/AddReview";
import AddedReview from "./components/AddedReview/AddedReview";

function App() {

 return (

  <BrowserRouter>

   <Routes>

    <Route
     path="/"
     element={<Home />}
    />

    <Route
     path="/login"
     element={<Login />}
    />

    <Route
     path="/register"
     element={<Register />}
    />

    <Route
     path="/dealer"
     element={<DealerDetails />}
    />

    <Route
     path="/add-review"
     element={<AddReview />}
    />

    <Route
      path="/added-review"
      element={<AddedReview />}
    />

   </Routes>

  </BrowserRouter>

 );

}

export default App;