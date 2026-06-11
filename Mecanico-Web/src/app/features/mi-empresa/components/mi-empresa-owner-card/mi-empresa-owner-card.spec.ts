import { ComponentFixture, TestBed } from "@angular/core/testing";

import { MiEmpresaOwnerCard } from "./mi-empresa-owner-card";

describe("MiEmpresaOwnerCard", () => {
	let component: MiEmpresaOwnerCard;
	let fixture: ComponentFixture<MiEmpresaOwnerCard>;

	beforeEach(async () => {
		await TestBed.configureTestingModule({
			imports: [MiEmpresaOwnerCard],
		}).compileComponents();

		fixture = TestBed.createComponent(MiEmpresaOwnerCard);
		component = fixture.componentInstance;
		await fixture.whenStable();
	});

	it("should create", () => {
		expect(component).toBeTruthy();
	});
});
