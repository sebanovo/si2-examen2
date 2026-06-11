import { Component } from "@angular/core";
import { PublicNavbar } from "../../../widgets/public/public-navbar/public-navbar";

@Component({
	selector: "app-public-page",
	imports: [PublicNavbar],
	templateUrl: "./public-page.html",
	styleUrl: "./public-page.css",
})
export class PublicPage {}
