import { ComponentFixture, TestBed } from "@angular/core/testing";

import { MiEmpresaHero } from "./mi-empresa-hero";

describe("MiEmpresaHero", () => {
	let component: MiEmpresaHero;
	let fixture: ComponentFixture<MiEmpresaHero>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [MiEmpresaHero],
		}).compileComponents();

		fixture = TestBed.createComponent(MiEmpresaHero);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
