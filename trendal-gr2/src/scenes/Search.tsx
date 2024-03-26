import React, { useState } from "react";

const SearchBar: React.FC = () => {
  const [searchText, setSearchText] = useState("");

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchText(event.target.value);
  };

  const handleSearch = () => {
    console.log("Search Text:", searchText);
  };

  return (
    <div className="search-bar-container">
      <button onClick={handleSearch} className="search-button"></button>
      <input
        type="text"
        placeholder="Enter search text..."
        value={searchText}
        onChange={handleInputChange}
      />
    </div>
  );
};

export default SearchBar;
