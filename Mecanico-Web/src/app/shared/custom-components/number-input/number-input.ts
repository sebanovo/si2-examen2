import { Component, input } from "@angular/core";
import { FormControl, ReactiveFormsModule } from "@angular/forms";
import { NgIcon, provideIcons } from "@ng-icons/core";
import { lucidePhone } from "@ng-icons/lucide";
import { HlmFieldImports } from "@shared/ui/field";
import { HlmInputImports } from "@shared/ui/input";

@Component({
	selector: "app-number-input",
	imports: [ReactiveFormsModule, HlmFieldImports, HlmInputImports, NgIcon],
	providers: [provideIcons({ lucidePhone })],
	templateUrl: "./number-input.html",
	styleUrl: "./number-input.css",
})
export class NumberInput {
	readonly control = input.required<FormControl<string>>();
	readonly inputId = input.required<string>();

	readonly label = input<string>("");
	readonly placeholder = input<string>("");
	readonly description = input<string>("");

	readonly icon = input<string | null>(null);

	// mensajes configurables
	readonly requiredMessage = input<string>("Este campo es obligatorio.");
	readonly minLengthMessage = input<string>("Debe contener minimo 8 numeros");
	readonly patternMessage = input<string>("Ingrese solo numeros");
}
