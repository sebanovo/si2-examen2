import { ChangeDetectionStrategy, Component, input } from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucideMail, lucidePhone, lucideUser } from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmCardImports } from "@shared/ui/card";
import { MiEmpresa } from "../../models/mi-empresa.types";

@Component({
	selector: "app-mi-empresa-owner-card",
	imports: [NgIcon, HlmBadgeImports, HlmCardImports],
	providers: [provideIcons({ lucideUser, lucideMail, lucidePhone })],
	host: {
		style: "display: block",
	},
	templateUrl: "./mi-empresa-owner-card.html",
	styleUrl: "./mi-empresa-owner-card.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class MiEmpresaOwnerCard {
	readonly empresa = input.required<MiEmpresa | null>();
}
