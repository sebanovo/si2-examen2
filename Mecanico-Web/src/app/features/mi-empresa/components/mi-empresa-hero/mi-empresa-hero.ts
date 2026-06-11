import {
	ChangeDetectionStrategy,
	Component,
	input,
	output,
} from "@angular/core";
import { NgIcon, provideIcons } from "@ng-icons/core";
import {
	lucideBadgeCheck,
	lucideBuilding2,
	lucideCheck,
	lucideMapPin,
	lucidePencil,
} from "@ng-icons/lucide";

import { HlmBadgeImports } from "@shared/ui/badge";
import { HlmButtonImports } from "@shared/ui/button";
import { MiEmpresa } from "../../models/mi-empresa.types";

@Component({
	selector: "app-mi-empresa-hero",
	imports: [NgIcon, HlmBadgeImports, HlmButtonImports],
	providers: [
		provideIcons({
			lucideBuilding2,
			lucideMapPin,
			lucidePencil,
			lucideCheck,
			lucideBadgeCheck,
		}),
	],
	host: {
		style: "display: block",
	},
	templateUrl: "./mi-empresa-hero.html",
	styleUrl: "./mi-empresa-hero.css",
	changeDetection: ChangeDetectionStrategy.OnPush,
})
export class MiEmpresaHero {
	readonly empresa = input.required<MiEmpresa | null>();
	readonly editMode = input(false);

	readonly editClick = output<void>();

	onEditClick(): void {
		this.editClick.emit();
	}
}
