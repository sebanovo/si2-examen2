import { Component } from "@angular/core";
import { RouterOutlet } from "@angular/router";

import { PublicFooter } from "../../components/public-footer/public-footer";
import { PublicNavbar } from "../../components/public-navbar/public-navbar";
// import { PublicHeader } from '../../components/public-header/public-header';

@Component({
	selector: "app-public-layout",
	standalone: true,
	imports: [RouterOutlet, PublicNavbar, PublicFooter],
	templateUrl: "./public-layout.html",
	styleUrl: "./public-layout.css",
})
export class PublicLayout {}
