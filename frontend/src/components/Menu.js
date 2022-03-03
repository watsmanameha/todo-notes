import React from "react";
import MenuItem from "@material-ui/core/MenuItem";
import Menu from "@material-ui/core/Menu";

const MenuApp = () => {
	return (
		<div>
			<Menu open>
				<MenuItem>All Users</MenuItem>
				<MenuItem>My Profile</MenuItem>
				<MenuItem>TODO</MenuItem>
			</Menu>
		</div>
	);
};

export default MenuApp;
